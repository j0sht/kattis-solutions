'''
Input:
    - Given a sequence of up to 2000 commands, one per line, ending
      at EOF.
    - All tokens within a command are separated by single spaces
    - Each command is either a:
        - Definition:
            - Format: def x y
            - x is a variable name
            - y is an int in range [-1000, 1000]
            * No two variable have same value at same time
            * If x had been defined previously, its value is
              replaced by y

        - Calculation:
            - Starts with word calc
            - Followed by one to 15 more variable names, separated
              by addition or subtraction operators.
            - End of calc command is an equal sign.
            - Ex) "calc foo + bar - car ="

        - Clear
            - Instructs program to forget all definitions

Output:
    - For each calculation, produce the value of the calculation
    - If there is not a variable for the result, or some variable
      in the calculation has not been defined, then result of the
      calculation should be 'unknown'
    * The name 'unknown' is never used as a variable in the input.
'''
class Calculator:
    __name_to_val = dict()
    __val_to_name = dict()

    def __str__(self):
        s = str(self.__name_to_val) + '\n'
        return s + str(self.__val_to_name)
    
    # Adding definition to calculator
    def update(self, var, val):
        prev_name = self.__val_to_name.get(val)
        val_exists = self.__name_to_val.get(var)
        if (prev_name):
            # Remove old reference to val in __name_to_val
            del self.__name_to_val[prev_name]
        if (val_exists):
            # Remove old reference to name in __val_to_name
            del self.__val_to_name[val_exists]

        # Preform update
        self.__name_to_val[var] = val
        self.__val_to_name[val] = var

    # Clearing calculator state
    def clear(self):
        self.__name_to_val = dict()
        self.__val_to_name = dict()

    # Perform calcuation
    def calculate(self, tokens):
        result = 0

        while len(tokens) > 0:
            token = tokens.pop(0)
            if (token == '+' or token == '-'):
                # Get next variable name
                next_name = tokens.pop(0)
                # See if exists in __name_to_val
                val = self.__name_to_val.get(next_name)
                if (val != None):
                    # Add or subtract val to/from result
                    if (token == '+'):
                        result += val
                    else:
                        result -= val
                else:
                    # Invalid variable name, return None
                    return None
            else:
                # Variable name, set result to its value if found
                val = self.__name_to_val.get(token)
                if (val != None):
                    result = val
                else:
                    # Invalid variable name, return None
                    return None

        return result

    def name_for_value(self, val):
        return self.__val_to_name.get(val)

def main():
    import sys

    calc = Calculator()
    
    # Get all commands from stdin
    command_strings = sys.stdin.readlines()

    # Iterate through each command
    for command_str in command_strings:
        # Remove newline character
        command_str = command_str.strip()
        
        # Tokenize command
        command_tokens = command_str.split()

        # Perform action
        action = command_tokens[0]
        if action == 'def':
            # Add/update value of variable
            name, val = command_tokens[1], int(command_tokens[2])
            calc.update(name, val)

        elif action == 'clear':
            # Clear calculator state
            calc.clear()

        else:
            # Get tokens other than first and last
            tokens = command_tokens[1:-1]
            # Perform calculation
            result = calc.calculate(tokens)
            # Initialize result output to 'unknown'
            output = 'unknown'
            if result != None:
                # Result is an int, try to get name for result
                name = calc.name_for_value(result)
                if name != None:
                    # Valid value, set output to value's name
                    output = name
            # Print the calc command and its resulting output
            print(' '.join(command_tokens[1:]) + ' ' + output)
                
if __name__ == '__main__':
    main()

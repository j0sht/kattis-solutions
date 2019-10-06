'''
link to problem: https://open.kattis.com/problems/polish
'''
def is_operator(token):
    return token == '+' or token == '-' or token == '*'

def is_number(token):
    try:
        num = int(token)
        return True
    except:
        return False

def is_symbol(token):
    not_op_or_num = not is_operator(token) and not is_number(token)
    len_at_most_2 = len(token) == 1 or len(token) == 2
    return not_op_or_num and len_at_most_2

def simplify(tokens):
    # Get first token
    token = tokens.pop(0)
    if is_number(token):
        return int(token)
    elif is_symbol(token):
        return token
    else: # must be an operator
        expr1 = simplify(tokens)
        expr2 = simplify(tokens)
        both_nums = is_number(expr1) and is_number(expr2)
        if token == '+' and both_nums:
            return expr1 + expr2
        elif token == '-' and both_nums:
            return expr1 - expr2
        elif token == '*' and both_nums:
            return expr1 * expr2
        else:
            return token + ' ' + str(expr1) + ' ' + str(expr2)

def main():
    import sys

    for (index, line) in enumerate(sys.stdin):
        raw_tokens = line.split()
        tokens = [token.strip() for token in raw_tokens]
        simplified = simplify(tokens)
        is_num = is_number(simplified)
        output = 'Case %d: %d' if is_num else 'Case %d: %s'
        print(output % ((index+1), simplified))

if __name__ == '__main__':
    main()

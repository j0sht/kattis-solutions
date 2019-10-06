'''
link to problem: https://open.kattis.com/problems/alphabetanimals
'''
def main():
    import sys

    # Read data
    data = sys.stdin.readlines()

    # Get last used word, and its last letter
    last_used = data.pop(0).strip()
    last_char = last_used[-1]

    # Ignore number of unused valid plays
    data.pop(0)

    # Index unused words by there first character
    first_char_map = dict()
    for unused in data:
        first_char = unused[0]
        if first_char_map.get(first_char):
            first_char_map[first_char].append(unused.strip())
        else:
            first_char_map[first_char] = [unused.strip()]
    
    # Get possible plays
    possible_plays = first_char_map.get(last_char)

    # Print '?' if there are no possible plays
    if possible_plays == None:
        print('?')
        return

    # See if there is a play that eliminates next player, print it with '!'
    for play in possible_plays:
        # Get last character
        last_char = play[-1]
        # Check if there are no possible plays with last char
        # of this potential play
        if first_char_map.get(last_char) == None:
            print(play + '!')
            return
        else:
            # Check if last_char equals first_char of play
            if last_char == play[0]:
                # Check if list of potential plays without this play
                # is empty. If so, print with '!'
                if len(first_char_map[last_char]) == 1:
                    print(play + '!')
                    return

    # Print first possible play
    print(possible_plays[0])

if __name__ == '__main__':
    main()

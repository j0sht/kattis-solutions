'''
Following code doesn't pass all tests on kattis
'''
def get_data():
    import sys

    # Read data
    raw_data = sys.stdin.readlines()

    # Ignore number of restaurants
    raw_data.pop(0)

    # Initialize dictionary with restaurant name keys and menu items
    names_and_items = dict()

    while len(raw_data) > 0:
        # Get number of items
        num_items = int(raw_data.pop(0))
        # Get restaurant name
        name = raw_data.pop(0).strip()
        # Initialize items
        items = []
        for _ in range(0, num_items):
            items.append(raw_data.pop(0).strip())
        # Insert restaurant and menu items
        names_and_items[name] = items

    # Return restaurant names and items
    return names_and_items

def check_peasoup_and_pancakes(items):
    import re
    peasoup, pancakes = False, False
    for item in items:
        if re.search('pea\s*soup', item):
            peasoup = True
        if re.search('pancakes', item):
            pancakes = True
        if peasoup and pancakes:
            break
    return peasoup and pancakes

def main():
    names_and_items = get_data()
    have_peasoup_and_pancakes = []
    names = []
    for (name, items) in names_and_items.items():
        names.append(name)
        if check_peasoup_and_pancakes(items):
            have_peasoup_and_pancakes.append(name)

    if len(have_peasoup_and_pancakes) == 1:
        for name in names:
            if name in have_peasoup_and_pancakes:
                print(name[:100])
                return
    else:
        print("Anywhere is fine I guess")
        
if __name__ == '__main__':
    main()

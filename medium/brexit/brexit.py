import sys

def remove_country(country_rels, rel_count, home_id, removal_stack):
    c_id = removal_stack.pop()
    
    # If c_id is the home country, print leave and finish program
    if c_id == home_id:
        print('leave')
        sys.exit(0)

    if country_rels.get(c_id):
        if rel_count.get(c_id):
            # Set curr to 0
            init, curr = rel_count[c_id]
            curr = 0
            rel_count[c_id] = init, curr

        # Remove reference to c_id from partners, decrement their counts
        partners = country_rels[c_id]
        while partners:
            partner = partners.pop()
            if rel_count.get(partner):
                # Decrement relationship count
                init, curr = rel_count[partner]
                curr -= 1
                rel_count[partner] = init, curr
            if country_rels.get(partner):
                # Remove c_id from partner's relations
                if c_id in country_rels[partner]:
                    country_rels[partner].remove(c_id)
            if (curr/init) <= 0.5:
                removal_stack.append(partner)

def main():
    # Read input
    read_first_line = False
    rel_count = dict()
    country_rels = dict()
    rels = set()
    for line in sys.stdin:
        if not read_first_line:
            first_line_data = line.split()
            number_of_countries = int(first_line_data[0])
            number_of_partnerships = int(first_line_data[1])
            home_country_id = int(first_line_data[2])
            first_to_leave = int(first_line_data[3])
            read_first_line = True
            continue
        countries = [int(s) for s in line.split()]
        country_a = countries[0]
        country_b = countries[1]
        if rel_count.get(country_a):
            initial, curr = rel_count[country_a]
            initial += 1
            curr += 1
            rel_count[country_a] = initial, curr
        else:
            rel_count[country_a] = 1, 1
        if country_rels.get(country_a):
            country_rels[country_a].add(country_b)
        else:
            country_rels[country_a] = {country_b}
        if rel_count.get(country_b):
            initial, curr = rel_count[country_b]
            initial += 1
            curr += 1
            rel_count[country_b] = initial, curr
        else:
            rel_count[country_b] = 1, 1
        if country_rels.get(country_b):
            country_rels[country_b].add(country_a)
        else:
            country_rels[country_b] = {country_a}

    # Compute answer
    removal_stack = [first_to_leave]
    while len(removal_stack) > 0:
        remove_country(country_rels, rel_count, home_country_id, removal_stack)

    init, curr = rel_count[home_country_id]
    if (curr/init) <= 0.5:
        print('leave')
    else:
        print('stay')    
        
if __name__ == '__main__':
    main()

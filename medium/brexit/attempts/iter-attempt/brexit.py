count = 0

def cascade(rels, rel_count, c_id):
    global count
    count += 1
    # Get relations with first to leave, and affected partners
    affected_partners = []
    rels_to_remove = []
    for rel in rels:
        if rel[0] == c_id:
            affected_partners.append(rel[1])
            rels_to_remove.append(rel)
        elif rel[1] == c_id:
            affected_partners.append(rel[0])
            rels_to_remove.append(rel)

    # Remove rels_to_remove
    for rel in rels_to_remove:
        rels.remove(rel)

    # Set count of leaver to 0
    init, curr = rel_count[c_id]
    curr = 0
    rel_count[c_id] = init, curr

    # Decrement count of affected partners
    for partner in affected_partners:
        init, curr = rel_count[partner]
        curr -= 1
        rel_count[partner] = init, curr
        # Check if curr-to-init ratio <= 50%
        if (curr/init) <= 0.5:
            # Remove its relations
            cascade(rels, rel_count, partner)
            
def main():
    import sys

    data = sys.stdin.readlines()
    first_line_data = data.pop(0).split()

    number_of_countries = int(first_line_data[0])
    number_of_partnerships = int(first_line_data[1])
    home_country_id = int(first_line_data[2])
    first_to_leave = int(first_line_data[3])

    rel_count = dict()
    rels = []
    for relationship in data:
        countries = [int(s) for s in relationship.split()]
        rels.append(countries)
        country_a = countries[0]
        country_b = countries[1]
        if rel_count.get(country_a):
            initial, curr = rel_count[country_a]
            initial += 1
            curr += 1
            rel_count[country_a] = initial, curr
        else:
            rel_count[country_a] = 1, 1
        if rel_count.get(country_b):
            initial, curr = rel_count[country_b]
            initial += 1
            curr += 1
            rel_count[country_b] = initial, curr
        else:
            rel_count[country_b] = 1, 1

    cascade(rels, rel_count, first_to_leave)
    home_init, home_curr = rel_count[home_country_id]
    if (home_curr/home_init) <= 0.5:
        print('leave')
    else:
        print('stay')
        
if __name__ == '__main__':
    main()

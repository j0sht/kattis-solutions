class Country:
    number_id = 0
    __initial_number_of_rels = 0
    __relationships = set()
    __leave = False

    def __init__(self, number_id, relationships):
        self.number_id = number_id
        self.__relationships = relationships
        self.__initial_number_of_rels = len(relationships)
        if self.__initial_number_of_rels == 0:
            self.__leave = True

    def __str__(self):
        s = 'Country: ' + str(self.number_id)
        s += '; Init Rs: ' + str(self.__initial_number_of_rels)
        s += '; rels: ' + str(self.__relationships)
        s += '; status: ' + str(self.__leave)
        return s

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.number_id == other.number_id

    def has_relation(self, number):
        return number in self.__relationships

    def remove_relationship(self, number):
        if not self.__leave:
            self.__relationships.remove(number)
            ratio = len(self.__relationships) / self.__initial_number_of_rels
            if ratio <= 0.5:
                self.__leave = True

    def get_relations(self):
        return self.__relationships

    def is_leaving(self):
        return self.__leave

class CountryManager:
    __home_country = 0
    __home_country_left = False
    __countries = dict()

    def __init__(self, home_country, relationships):
        self.__home_country = home_country
        rels = dict()
        for relationship in relationships:
            countryA = relationship[0]
            countryB = relationship[1]
            if rels.get(countryA):
                rels[countryA].add(countryB)
            else:
                rels[countryA] = {countryB}
            if rels.get(countryB):
                rels[countryB].add(countryA)
            else:
                rels[countryB] = {countryA}
        for (countryID, partnerships) in rels.items():
            country = Country(countryID, partnerships)
            self.__countries[countryID] = country

    def __str__(self):
        return str(self.__countries)

    def __repr__(self):
        return self.__str__()

    def debug(self):
        for c_id, country in self.__countries.items():
            print(c_id, ':', country)

    def remove_country(self, country_id):
        if country_id == self.__home_country:
            self.__home_country_left = True
        if self.__countries.get(country_id):
            country_leaving = self.__countries[country_id]
            relations = country_leaving.get_relations()
            print(relations)
            del self.__countries[country_id]
            for partner_id in relations:
                if self.__countries.get(partner_id):
                    partner = self.__countries[partner_id]
                    if partner.has_relation(country_id):
                        partner.remove_relationship(country_id)
                    if partner.is_leaving():
                        self.remove_country(partner_id)

    def home_country_left(self):
        return self.__home_country_left

    def get_call_count(self):
        return self.__count
            
def main():
    import sys

    data = sys.stdin.readlines()
    first_line_data = data.pop(0).split()

    number_of_countries = int(first_line_data[0])
    number_of_partnerships = int(first_line_data[1])
    home_country = int(first_line_data[2])
    first_to_leave = int(first_line_data[3])

    rels = []
    for relationship in data:
        relationship_strs = relationship.split()
        relationship_ints = [int(s) for s in relationship_strs]
        rels.append(relationship_ints)

    cm = CountryManager(home_country, rels)
    cm.remove_country(first_to_leave)
    print('leave' if cm.home_country_left() else 'stay')

if __name__ == '__main__':
    main()

people = [
    {"name": "Harry", "house": "Gryffindor"}
    , {"name": "Cho", "house": "Ravenclaw"}
    , {"name": "Draco", "house": "Slytherin"}
]

people.sort(key = lambda person: person["name"]) # take person as input, and output person["name"]

print(people)
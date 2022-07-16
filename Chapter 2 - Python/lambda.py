people = [                              # Dictionary inside of a list
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"}, 
    {"name": "Draco", "house": "Slytherin"}
]

 # to use a lambda instead of this
 # def f(person):
 #   return person["name"]

#people.sort(key = f)                    

people.sort(key = lambda person: person["name"])

print(people)

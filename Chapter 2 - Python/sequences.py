# STRINGS
name = "Harry"

print(name[0])

names = ["Harry", "Ron", "Hermione"]
print(names)
print(names[2])

# TUPLES
coordinateX = 10.0
coordinateY = 20.0  #Instead of these, as they will always be together, we can create a tuple

coordinate = (10.0, 20.0)

# LISTS
names = ["Harry", "Ron", "Hermione", "Ginny"] 
print(names[0])

names.append("Draco")    #As lists are mutable, I have functions to modify them

names.sort()             #.sort() orders the list alphabeticaly.

print(names)


# SETS
s = set()               # Creates an empty set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(s)
s.add(3)
print(s)                # Python will take the value, but will only show one reference, as is a set, and values will be unique. 

s.remove(2)
print(s)

print(f"The set has {len(s)} elements ")    #len(collection) gives the length of the collection given as an argument. 



# DICTIONARIES

houses = {"Harry" : "Gryffindor", "Draco":"Slytherin"}
print(houses["Harry"])

houses["Hermione"] = "Gryffindor"       #This adds a new key:value pair to the dict.

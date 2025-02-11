name = "andy" #this is immutable

print(id(name), name)

name = "andrew" #this won't change name to be andrew, it'll just make a seperate memory location for it

print(id(name), name)

name = "andy" #this will have the same memory location as the first name = "andy"

print(id(name), name)


dct = {} #dictionaries are mutable

dct["name"] = "andy"
print(id(dct), dct)

dct["name"] = "andrew" #this did not change the memory location, it just chanfed andy to andrew.
print(id(dct), dct)


#objects are also mutable!!
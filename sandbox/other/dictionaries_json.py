import json

#create a dictionary and save as json
dct = {}
dct["name"] = "andy"
dct["major"] = "data analytics"

dct["favorite_song"] = "crazy frog axel f"
dct["favorite_song"] = "i barely knew you" #since this is mutable, fav song will be changed to this
print(dct)

#to save it as a json file

file = open("andy_info.json", "w") #usually you put a full path so it adds to a specific folder
json.dump (dct, file, indent = 4)

#to load it back in
file = open("andy_info.json")
dct = json.load(file)


# #my dictionary
my_dct = {}
my_dct["food"] = "spaghetti"
my_dct["pasta"] = "spahetti noodles"
my_dct["sauce"] = "meat sauce"
print(my_dct)


try:
    file2 = open("spaghetti_recipe.json", "w")
    json.dump (dct, file2, indent = 4)
except:
    print("opening file failed")

with open("spaghetti_recipe.json") as file2:
    my_dct = json.load(file2)

my_dct["toppings"] = "cheese"

print(my_dct)
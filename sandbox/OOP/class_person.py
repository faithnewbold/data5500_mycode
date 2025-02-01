#a class is a blueprint and an object is what you make with it

import numpy as np

lst = [1, 2, 3, 4, 5]

names = ["andy", "julie", "deven", "zach", "bart"]

person = {"name" : "deven",
"age" : 22,
"home town" : "south bend", 
"favorite color" : "blue",
"hw_scores" : [95, 85, 99, 100, 99]}

def avg_hw_score(hw_scores):
    return np.mean(hw_scores)

deven = [22, "south bend", "blue"]

print(avg_hw_score(person["hw_scores"]))

class Person:
    def __init__(self, name, age, home_town, favorite_color, hw_scores):
        self.name = name
        self.age = age
        self.home_town = home_town
        self.favorite_color = favorite_color
        self.hw_scores = hw_scores

    def __str__(self):
        return self.name + " from " + self.home_town + " and their favorite color is: " + self.favorite_color + "\n"
    def avg_hw_score(self):
        return np.mean(self.hw_scores)

andy = Person("andy", 43, "Elmhurst", "aggie blue", [])
claire = Person("claire", 22, "Twin Falls", "blue", [100, 100, 100])

print(andy.name, andy.hw_scores, andy.avg_hw_score())
print(claire.name, claire.hw_scores, claire.avg_hw_score())

print(andy,claire)



#my class I created:

# class Instrument:
#     def __init__(self, )
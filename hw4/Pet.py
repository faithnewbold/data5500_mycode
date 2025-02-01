class Pet():
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    lifespans = {
        "dog": 13,
        "cat": 15,
        "rabbit": 10,
        "tortoise": 100,
        "horse": 25
    }

    def human_years(self):
        conversion_rates = {
            "dog": 7,
            "cat": 5,
            "rabbit": 8,
            "tortoise": 0.5,
            "horse": 3
        }

        if self.species in conversion_rates:
            return self.age * conversion_rates[self.species]
        else:
            return "Unknown species."

    def average_lifespan(self):
        if self.species in Pet.lifespans:
            return Pet.lifespans[self.species]
        else:
            return "Unknown species."

pet1 = Pet("Jovi", 6, "dog")
pet2 = Pet("Jack", 13, "cat")
pet3 = Pet("Henry", 76, "tortoise")

print(f"{pet1.name}, who is a {pet1.species}, is {pet1.human_years()} human years old, and their lifespan is {pet1.average_lifespan()}")
print(f"{pet2.name}, who is a {pet2.species}, is {pet2.human_years()} human years old, and their lifespan is {pet2.average_lifespan()}")
print(f"{pet3.name}, who is a {pet3.species}, is {pet3.human_years()} human years old, and their lifespan is {pet3.average_lifespan()}")


# chatgpt link:
# https://chatgpt.com/share/679d75df-b544-800d-9d39-fd9db72ac688
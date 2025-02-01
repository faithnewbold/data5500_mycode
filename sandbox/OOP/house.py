class House(): #this is the class/the blueprint. #you can also import this class definition onto another python file to use there
    def __init__(self, area_code, sq_ft, num_bedrms, num_bathrms, age_home, garage_code, tax_info):
        self.area_code = area_code
        self.sq_ft = sq_ft
        self.num_bathrms = num_bathrms
        self.num_bedrms = num_bedrms
        self.age_home = age_home
        self.garage_code = garage_code
        self.tax_info = tax_info

    def __str__(self):
        return "House with " + str(self.sq_ft) + " sq ft."

our_house = House(435, 3000, 3, 5, 0, 1234, 7) #this is the object/what we created from the blueprint

class Cottage(House): #this is a child class, it got all of it's data from the parent class(House). Since House is in the paranthesis, now Cottage is a derivative of House
    def __init__(self, area_code, sq_ft, num_bedrms, num_bathrms, age_home, garage_code, tax_info, air_bnb_rent):
        self.area_code = area_code
        self.sq_ft = sq_ft
        self.num_bathrms = num_bathrms
        self.num_bedrms = num_bedrms
        self.age_home = age_home
        self.garage_code = garage_code
        self.tax_info = tax_info
        self.air_bnb_rent = air_bnb_rent

    def __str__(self):
        return "Cottage with " + str(self.sq_ft) + " sq ft. and airbnb rent of " + str(self.air_bnb_rent)

fun_house = Cottage(630, 1500, 2, 3, 0, 1234, 8, 250)

print(fun_house)

print(our_house)

print(fun_house.sq_ft)


#programming activity: create a parent class, then create a child class based off of that, and then create a child object.
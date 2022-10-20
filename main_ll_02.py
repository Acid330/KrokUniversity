import random
import json

#1

class Project:

    def __init__(self, cost, miss_week=0):
        self.cost = cost
        self.miss_week = miss_week
        self.number = random.randint(11111, 99999)

    def cost_calc(self):
        if self.__class__.__name__ == "Standard":
            self.cost = self.cost
        elif self.__class__.__name__ == "Days_10":
            self.cost = self.cost + (self.cost * 0.6)
        elif self.__class__.__name__ == "Investor_Project":
            self.cost = self.cost - (self.cost * 0.2)
        return self.cost

    def miss(self):
        if self.miss_week > 0:
            self.cost = self.cost_calc()
            self.cost = self.cost - (self.cost * (self.miss_week * 0.05))
            if self.cost < 0:
                self.cost = "Free"
        else:
            self.cost = self.cost_calc()
            self.miss_week = 0
        return f"Cost: {self.cost}, Miss week:  {self.miss_week}"

    def writer(self):
        writer = f"Project ID: {self.number},Type: {self.__class__.__name__} ,{self.miss()}"
        return writer


class Standard(Project):
    def __str__(self):
        return f"{self.writer()}"


class Days_10(Project):
    def __str__(self):
        return f"{self.writer()}"


class Investor_Project(Project):
    def __str__(self):
        return f"{self.writer()}"

#2

class Stat:
    def __init__(self, sex, weight, color_skin, tatoo, color_hair=None):
        if sex == "man" or sex.lower() == "woman" or sex == "Man" or sex.lower() == "Woman":
            self.sex = sex
            if weight <= 35:
                raise "Weight can be 35 or less"
            self.weight = weight
            self.color_skin = color_skin
            self.tatoo = tatoo
            self.color_hair = color_hair
        else:
            raise ValueError("Wrong sex")

    def info(self):
        if self.__class__.__name__ == "Argonianine":
            self.color_hair = "This race cannot have hair"

        info = f"\nSex: {self.sex}\nHair: {self.color_hair}\nSkin: {self.color_skin}\nWeight: {self.weight}\nTatoo: {self.tatoo} "

        return info


class Argonianine(Stat):
    def __str__(self):
        return f"Race: {self.__class__.__name__} {self.info()}"


class Breton(Stat):
    def __str__(self):
        return f"Race: {self.__class__.__name__}, {self.info()}"


class Altmer(Stat):
    def __str__(self):
        return f"Race: {self.__class__.__name__}, {self.info()}"


class North(Stat):
    def __str__(self):
        return f"Race: {self.__class__.__name__}, {self.info()}"


class Dunmer(Stat):
    def __str__(self):
        return f"Race: {self.__class__.__name__}, {self.info()}"


class Kajit(Stat):
    def __str__(self):
        return f"Race: {self.__class__.__name__}, {self.info()}"

# print
#1
prj = Standard(100, 2)
prj1 = Days_10(100, 2)
prj2 = Investor_Project(100, 2)

info = prj.writer()

with open("data.json", "w") as x:
    json.dump(info, x)

info = open('data.json', )
res = json.load(info)

print(res, "\n")
#2
pers = Argonianine("man", 78, "Green", "On Face", "Black")
print(pers)

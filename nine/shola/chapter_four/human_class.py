class Human:
    name = "Shola"
    sex = "Male"
    nationality = "Nigerian"


class SecondHuman:
    def __init__(self, sex, name, nationality):
        self.name = name
        self.sex = sex
        self.nationality = nationality
        self.age = 0
        self.height = 0
        self.skin_tone = "Black"

    # you can create functions to update the variables that were already initialized to other values

    def set_age(self, age):
        self.age = age

    def set_height(self, height):
        self.height = height

    def set_skin_tone(self, skin_tone):
        self.skin_tone = skin_tone


# to create an object of class SecondHuman
dami = SecondHuman("male", "Dami", "Nigerian")

dami.height = 5.5
dami.age = 19
dami.skin_tone = "White"

print(dami.name, dami.age, dami.sex, dami.skin_tone)



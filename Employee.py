class Employee:
    def __init__(self, name, gander, age, university,rating):
        self.name = name
        self.gander = gander
        self.age = age
        self.university = university
        self.rating = rating

    def is_excellent(self):
        if self.rating >= 4.5:
            return True
        else:
            return False

class Animals:
    def __init__(self, typ, name, age):
        self.typ = typ
        self.name = name
        self.age = age

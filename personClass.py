import pickle

class person():
    def __init__(self, name, gender, age):
        self.name=name
        self.gender=gender
        self.age=age

    def __str__(self):
        return "{} {} {}". format(self.name, self.gender, self.age)
    

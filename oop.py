class Musician:
    def __init__(self, genre , country):
        self.genre = genre
        self.country = country


Bladee = Musician("hyperpop", "Sweden")
Perfume = Musician("EDM", "Japan")

print(Bladee.country)

class Artiste(Musician):
    pass


class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

Car.move(print("Driving 🚗"))

class Plane(Vehicle):
  pass
  def move(self):
    Plane.move(print("fly ✈️"))


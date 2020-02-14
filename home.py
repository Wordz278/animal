from animal import Animal
from cat import Cat
from dog import Dog


class Home:
    def __init__(self, pets = []):
        self.pets = pets

    def adopt_Pets(self,pet):
        for each in self.pets:
            if each == pet:
                raise Exception("You cant adopt the same pet twice.")
        self.pets.append(pet)

if __name__ == "__main__":
    home = Home()
    dog1 = Dog("Rax", "Barks")
    cat1 = Cat("Stormy", "meows")
    home.adopt_Pets(dog1)
    print(home.pets[0].name)

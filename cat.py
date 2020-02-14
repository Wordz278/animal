from animal import Animal

class Cat(Animal):
    def __init__(self, name, sounds):
        super().__init__(name, sounds)

    def food(self):
        print(self.name + " eats")

    def sound(self):
        print(self.sounds,"meows")


print("==========Cat==============")
cat = Cat("Stormy", "Cat")
cat.food()
cat.sound()
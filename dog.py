from animal import Animal

class Dog(Animal):
    def __init__(self, name, sounds):
        super().__init__(name, sounds)

    def food(self):
        print(self.name + " eats")

    def sound(self):
        print(self.sounds + " barks")

print("==========Dog==============")
dog = Animal("Rax", "Dog")
dog.food()
dog.sound()
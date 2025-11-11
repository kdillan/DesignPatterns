class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

class Cow(Animal):
    def sound(self):
        return "Moo!"

def make_sound(Animal):
    print(Animal.sound())

# Creating instances of different animals
dog = Dog()
cat = Cat()
cow = Cow()

# Calling the make_sound function with different animal objects
make_sound(dog)  # Output: Woof!
make_sound(cat)  # Output: Meow!
make_sound(cow)  # Output: Moo!

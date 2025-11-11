'''
In this example:
There is a composition relationship between the Girl class and the Pet class. The Girl class contains an instance of the Pet class as one of its attributes.
The Pet class represents a generic pet with a name and a species. It has an abstract method make_sound(), which is overridden by its subclasses.
The Dog  classes are subclasses of Pet representing specific types of pets. They override the make_sound() method to provide their specific sound.
The Girl class represents a girl who has a pet. It contains an attribute pet that holds an instance of the Pet class.
The introduce() method of the Girl class allows a girl to introduce herself along with information about her pet.
'''
class Pet:
    def __init__(self, name, species, age, weight):
        self.name = name
        self.species = species
        self.age = age
        self.weight = weight

    def make_sound(self):
        pass  # Abstract method, to be overridden by subclasses
class Dog(Pet):
    def make_sound(self):
        return "Bark, bark!"
class Girl:
    def __init__(self, name, pet):
        self.name = name
        self.pet = pet
    def introduce(self):
        return f"Hi! My name is {self.name}. I love my pet {self.pet.species} named {self.pet.name}.  {self.pet.name} is {self.pet.age} years old and he weighs {self.pet.weight} lbs. "
# Usage
dog = Dog("Dallas", "dog", 14, "56")
girl = Girl("Katie", dog)

print(girl.introduce())  # Output: Hi! My name is Katie. I love my pet dog named Dallas.  He is 14 years old and he weighs 56 lbs.

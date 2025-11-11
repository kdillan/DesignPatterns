'''In this example:
Fruit is the base class with a method grow().
Blue and Red are subclasses of Fruit inheriting the grow() method. They override the grow() method to provide their specific implementation.
FruitFactory is a factory class responsible for creating instances of Blue and Red based on the given fruit color type.
Fruit Factory uses inheritance relationship by creating instances of Blue and Red, which are subclasses of Fruit. This allows it to return instances of the appropriate subclasses based on the input.
This example demonstrates inheritance is used in the Factory Method design pattern to create objects without specifying the exact class of the object that will be created.
'''
class Fruit:
    def grow(self):
        pass
class BlueFruit(Fruit):
    def grow(self):
        return "Farm will be harvesting Blueberries"
class RedFruit(Fruit):
    def grow(self):
        return "Farm will be harvesting Strawberries!"
class FruitFactory:
    def get_fruit(self, fruit_type):
        if fruit_type == "blue":
            return BlueFruit()
        elif fruit_type == "red":
            return RedFruit()
        else:
            raise ValueError("Selected wrong fruit color")
# Usage
farm = FruitFactory()
blue = farm.get_fruit("blue")
red  = farm.get_fruit("red")

print(blue.grow())  # Blueberries!
print(red.grow())  # Output: Strawberries!
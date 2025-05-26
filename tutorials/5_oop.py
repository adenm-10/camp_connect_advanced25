# This defines a class called Dog
class Dog:
    # The __init__ method runs when we create a new Dog
    def __init__(self, name, age):
        self.name = name  # Each dog has a name
        self.age = age    # Each dog has an age

    # A method to make the dog bark
    def bark(self):
        print(f"{self.name} says woof!")

    # A method to show the dog's information
    def show_info(self):
        print(f"This is {self.name} and they are {self.age} years old.")

# Creating (instantiating) two dogs
dog1 = Dog("Buddy", 3)
dog2 = Dog("Luna", 5)

# Calling methods
dog1.bark()         # Output: Buddy says woof!
dog2.show_info()    # Output: This is Luna and they are 5 years old.

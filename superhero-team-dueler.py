# class Dog:
#     greeting = "Woof!"
#
#     def __init__(self, name):
#         self.name = name
#
#     def bark(self):
#         print(self.greeting)
#
# my_dog = Dog("Spot")
# print(my_dog.name)
#
# my_other_Dog = Dog("Annie")
# print(my_other_Dog.name)
#
# my_first_dog = Dog("Annie")
# my_second_dog = Dog("Wyatt")
#
# print(my_first_dog.name)
# print(my_second_dog.name)
#
# my_first_dog.bark()
# my_second_dog.bark()


import random

class Ability:
    def __init__(self, name, attack_strength):
        # Initialize starting values
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        # Return attack value
        lowest_attack_value = self.attack_strength // 2
        random_attack_value = random.randint(lowest_attack_value, self.attack_strength)
        return random_attack_value

    def update_attack(self, attack_strength):
        # Update attack value

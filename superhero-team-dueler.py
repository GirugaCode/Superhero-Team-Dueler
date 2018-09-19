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

class Hero:
    def __init__(self,name):
        self.abilities = list()
        self.name = name

    def add_ability(self, ability):
        # Append ability to self.abilities
        self.abilities.append(ability)

    def attack(self):
        # Call the attack method on every ability in our ability list
        total_attack = 0
        # Add up and return the total of all attacks
        for add_attack in self.abilities:
            total_attack += add_attack.attack()
        return total_attack

class Ability:
    def __init__(self, name, attack_strength):
        # Initialize starting values
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        # Calculate lowest attack value as an integer.
        lowest_attack_value = self.attack_strength // 2
        # Use random.randint(a, b) to select a random attack value.
        random_attack_value = random.randint(lowest_attack_value, self.attack_strength)
        # Return attack value between 0 and the full attack
        return random_attack_value

    def update_attack(self, attack_strength):
        # Update attack value
        self.attack_strength = attack_strength


if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())

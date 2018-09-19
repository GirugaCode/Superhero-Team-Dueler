import random

class Hero:
    def __init__(self, name):
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

class Team:
    def __init__(self, team_name):
        """Intantiate resources"""
        self.heroes = list()
        self.name = team_name

    def add_hero(self, Hero):
        """Add Hero object to heroes list."""
        self.heroes.append(Hero)

    def remove_hero(self, name):
        """
        Remove hero from heroes list.
        If Hero isn't found return 0.
        """
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
        return 0

    def find_hero(self, name):
        """
        Find and return hero from heroes list.
        If Hero isn't found return 0.
        """
        for hero in self.heroes:
            if hero.name == name:
                return hero
        return 0

    def view_all_heroes(self):
        """Print out all heroes to the console."""
        for hero in self.heroes:
            print(hero.name)

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

class Weapon(Ability):
    def attack(self):
        return random.randint(0, self.attack_strength)




if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())

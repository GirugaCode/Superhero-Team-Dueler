import random
import os


class Hero:
    def __init__(self, name, health = 100):
        self.abilities = list()
        self.name = name
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        # Append ability to self.abilities
        self.abilities.append(ability)

    def add_armor(self, armor):
        # Append ability to self.abilities
        self.armors.append(armor)

    def attack(self):

        # Call the attack method on every ability in our ability list
        total_attack = 0
        # Add up and return the total of all attacks
        for add_attack in self.abilities:
            total_attack += add_attack.attack()
        return total_attack

    def defend(self):
        """
        This method should run the defend method on each piece of armor and calculate the total defense.
        If the hero's health is 0, the hero is out of play and should return 0 defense points.
        """
        total_armor = 0
        for add_defense in self.armors:
            total_armor += add_defense.defend()
            if self.start_health == 0:
                self.heroes.remove(hero)
        return total_armor
        return 0

    def take_damage(self, damage_amt):
        """
        This method should subtract the damage amount from the
        hero's health.
        If the hero dies update number of deaths.
        """
        if self.health > 0:
            self.health -= damage_amt
            if self.health <= 0:
                self.deaths += 1
        return self.deaths

    def add_kill(self, num_kills):
        """
        This method should add the number of kills to self.kills
        """
        self.kills += num_kills

    def listAbilities(self):
        my_abilities = list()
        for ability in self.abilities:
            my_abilities.append((ability.name, ability.attack_strength))
        return my_abilities

    def listArmors(self):
        myArmors = list()
        for armor in self.armors:
            myArmors.append((armor.name, armor.defense))
        return myArmors

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
        myHeroes = ""
        print(len(self.heroes))
        for hero in self.heroes:
            myHeroes += hero.name
        print("Hero str: {}".format(myHeroes))
        return myHeroes


    def attack(self, other_team):
        """
        This method should total our teams attack strength and call the defend()
        method on the rival team that is passed in.
        It should call add_kill() on each hero with the number of kills made.
        """
        total_attack = 0
        for hero in self.heroes:
            total_attack += hero.attack()

        enemy_team = other_team.defend(total_attack)
        for hero in self.heroes:
            hero.add_kill(enemy_team)
        return total_attack

    def defend(self, damage_amt):
        """
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should be
        evenly distributed amongst all heroes with the deal_damage() method.

        Return number of heroes killed in attack.
        """
        team_total_defense = 0
        for hero in self.heroes:
            team_total_defense += hero.defend()

        if damage_amt > team_total_defense:
            dead_heroes = self.deal_damage(damage_amt - team_total_defense)
            return dead_heroes

    def deal_damage(self, damage):
        """
        Divide the total damage amongst all heroes.
        Return the number of heroes that died in attack.
        """
        kills = 0
        damage = damage // len(self.heroes)
        for total_damage in self.heroes:
            total_damage.take_damage(damage)
            kills += total_damage.deaths
        return kills

    def revive_heroes(self, health = 100):
        """
        This method should reset all heroes health to their
        original starting value.
        """
        for hero in self.heroes:
            hero.health = hero.start_health

    def stats(self):
        """
        This method should print the ratio of kills/deaths for each member of the team to the screen.
        This data must be output to the terminal.
        """
        for hero_stats in self.heroes:
            print(hero_stats.name + " K/D: " + str(hero_stats.kills) + "/" + str(hero_stats.deaths))

    def update_kills(self, kills):
        """
        This method should update each hero when there is a team kill.
        """
        total_team_kills = 0
        for hero in self.heroes:
            total_team_kills += hero.kills
        return total_team_kills





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
    def __init__(self, name, attack_strength):
        super().__init__(name, attack_strength)
    def attack(self):
        """
        This method should should return a random value
        between 0 and the full attack power of the weapon.
        Hint: The attack power is inherited.
        """
        low = self.attack_strength // 2
        return random.randint(low, self.attack_strength)

class Armor:
    def __init__(self, name, defense):
        """ Instantiate name and defense strength. """
        self.name = name
        self.defense_strength = int(defense)

    def defend(self):
        """
        Return a random value between 0 and the
        initalized defend strength.
        """
        return random.randint(0, self.defense_strength)

class Arena:
    def __init__(self, team_one, team_two):
        """ Declare variables"""
        self.team_one = team_one
        self.team_two = team_two

    def user_input(self, prompt):
        user_input = input(prompt)
        return user_input

    def build_team_one(self):
        """
        This method should allow a user to build team one.
        """
        hero_one = Hero(self.user_input("What is the name of your first hero? "))
        ability_name = self.user_input("Whats the heroes power? ")
        power_stats = len(ability_name) * random.randint(1, 5) * 10
        ability_stats = Ability(ability_name, int(power_stats))
        hero_one.add_ability(ability_stats)
        weapon_one = Weapon(self.user_input("What weapon do they use? "), random.randint(1, 5) * 10)
        hero_one.add_ability(weapon_one)

        hero_two = Hero(self.user_input("What is the name of your second hero? "))
        ability_name_two = self.user_input("What is the heroes power? ")
        power_stats_two = len(ability_name_two) * random.randint(1, 5) * 10
        ability_stats_two = Ability(ability_name_two, int(power_stats_two))
        hero_two.add_ability(ability_stats_two)
        weapon_two = Weapon(self.user_input("What weapon do they use? "), random.randint(1, 5) * 10)
        hero_two.add_ability(weapon_two)


        self.team_one.add_hero(hero_one)
        self.team_one.add_hero(hero_two)

    def build_team_two(self):
        """
        This method should allow user to build team two.
        """
        os.system("clear")
        print("TIME TO BUILD THE SECOND TEAM!")
        hero_one = Hero(self.user_input("What is the name of your first hero? "))
        ability_name = self.user_input("Whats the heroes power? ")
        power_stats = len(ability_name) * random.randint(1, 5) * 10
        ability_stats = Ability(ability_name, int(power_stats))
        hero_one.add_ability(ability_stats)
        weapon_one = Weapon(self.user_input("What weapon do they use? "), random.randint(1, 5) * 10)
        hero_one.add_ability(weapon_one)

        hero_two = Hero(self.user_input("What is the name of your second hero? "))
        ability_name_two = self.user_input("What is the heroes power? ")
        power_stats_two = len(ability_name_two) * random.randint(1, 5) * 10
        ability_stats_two = Ability(ability_name_two, int(power_stats_two))
        hero_two.add_ability(ability_stats_two)
        weapon_two = Weapon(self.user_input("What weapon do they use? "), random.randint(1, 5) * 10)
        hero_two.add_ability(weapon_two)


        self.team_two.add_hero(hero_one)
        self.team_two.add_hero(hero_two)

    def team_battle(self):
        """
        This method should continue to battle teams until
        one or both teams are dead.
        """
        deaths_one = 0
        deaths_two = 0

        while deaths_one < len(self.team_one.heroes) and deaths_two < len(self.team_two.heroes):
            self.team_one.attack(self.team_two)
            self.team_two.attack(self.team_one)
            for i in self.team_one.heroes:
                deaths_one += i.deaths
            for i in self.team_two.heroes:
                deaths_two += i.deaths


    def show_stats(self):
        """
        This method should print out the battle statistics
        including each heroes kill/death ratio.
        """
        print(self.team_one.name + " stats:")
        self.team_one.stats()
        print(self.team_two.name + " stats:")
        self.team_two.stats()

    def game_restart(self):
        choice = self.user_input("Do you want to battle again? [yes/no] ")
        if choice == "yes" or choice == "y" or choice == "Y":
            self.team_one.revive_heroes()
            self.team_two.revive_heroes()
            game_loop(self)




team_one = Team(input('Enter a team name: '))
team_two = Team(input('Enter a second team name: '))
arena = Arena(team_one, team_two)
arena.build_team_one()
arena.build_team_two()

def game_loop(arena):
    arena.team_battle()
    arena.show_stats()
    arena.game_restart()

game_loop(arena)

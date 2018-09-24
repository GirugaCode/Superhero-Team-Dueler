import random


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
        myHeroes = []
        for hero in self.heroes:
            myHeroes.append(hero.name)
        return myHeroes

    def attack(self, other_team):
        """
        This method should total our teams attack strength and call the defend()
        method on the rival team that is passed in.
        It should call add_kill() on each hero with the number of kills made.
        """
        totalAttack = 0
        for hero in self.heroes:
            totalAttack += hero.attack()

        # print('total atk: ' + str(totalAttack))

        enemiesDead = other_team.defend(totalAttack)

        for hero in self.heroes:
            hero.add_kill(enemiesDead)
        return totalAttack

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
        damage = damage_amt - team_total_defense
        self.deal_damage(damage)

        kills = 0
        if damage > 0:
            damage_per_hero = damage // len(self.heroes)
            for hero in self.heroes:
                dead = hero.take_damage(damage_per_hero)
                if dead == 1:
                    kills += 1
        return kills


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
            print(hero_stats.name + "K/D: " + str(hero_stats.kills) + "/" + str(hero_stats.deaths))

    def update_kills(self, kills):

        totalTeamKills = 0
        for hero in self.heroes:
            totalTeamKills += hero.kills
        return totalTeamKills

        """
        This method should update each hero when there is a team kill.
        """


		# rm = kills % len(self.heroes)
		# self.heroes[0].add_kill(rm)
		# kills = kills / len(self.heroes)
		# for i in self.heroes:
		# 	i.add_kill(kills)

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
        """
        This method should should return a random value
        between 0 and the full attack power of the weapon.
        Hint: The attack power is inherited.
        """
        return random.randint(0, self.attack_strength)

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

if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())

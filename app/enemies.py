import random;

class Goblin:
    def __init__(self):
        self.max_constitution = random.randint(10, 20)
        self.constitution = self.max_constitution
        self.strength = 8
        self.dexterity = 8
        self.intelligence = 2
        self.wisdom = 0
        self.charisma = 2
        self.armor = 10

    def attack_1(self):
        print(f"""\nThe goblin swings its club at you...""")
        attack_roll = random.randint(0, (10 + self.dexterity))
        print(f"""\nGoblin rolls a {attack_roll}""")
        if attack_roll >= pc.armor:
            damage = random.randint(1, self.strength)
            print(f"""\nThe goblin hits you with their club for {damage} damage!""")
        else:
            print(f"""\nThe goblin misses you with their attack!""")
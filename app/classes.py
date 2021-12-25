import random;

class Player:
    def __init__(self, player_class):
        self.player_class = player_class

    def spawn_class_object(self):
        if self.player_class == "Warrior":
            player2 = Warrior

class Warrior(Player):
    def __init__(self):
        self.max_constitution = 20
        self.constitution = 20
        self.strength = 10
        self.dexterity = 10
        self.intelligence = 10
        self.wisdom = 10
        self.charisma = 10
        self.armor = 10

    def basic_attack(self):
        print(f"""\nYou swing your sword at the goblin...""")
        attack_roll = random.randint(0, (10 + (self.dexterity)))
        print(f"""\nYou a {attack_roll}""")
        if attack_roll >= npc.armor:
            damage = random.randint(1, self.strength)
            print(f"""\nYou hit the goblin with your sword for {damage} damage!""")
        else:
            print(f"""\nYou miss the goblin with your attack!""")
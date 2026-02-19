# Enemy Classes for Super Bingo Game

class Enemy:
    """Basic Enemy Class"""
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self):
        return self.attack_power

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()

    def die(self):
        print(f'{self.name} has been defeated!')


class Goblin(Enemy):
    """Goblin Enemy Class"""
    def __init__(self):
        super().__init__(name='Goblin', health=30, attack_power=5)


class Troll(Enemy):
    """Troll Enemy Class"""
    def __init__(self):
        super().__init__(name='Troll', health=50, attack_power=10)
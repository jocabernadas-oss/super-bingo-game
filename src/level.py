class Level:
    def __init__(self, level_number):
        self.level_number = level_number
        self.difficulty = self.set_difficulty()

    def set_difficulty(self):
        if self.level_number == 1:
            return 'Easy'
        elif self.level_number == 2:
            return 'Medium'
        elif self.level_number == 3:
            return 'Hard'
        else:
            return 'Unknown'

    def __str__(self):
        return f'Level {self.level_number}: {self.difficulty}'

# Example usage:
if __name__ == '__main__':
    level1 = Level(1)
    print(level1)
    level2 = Level(2)
    print(level2)
    level3 = Level(3)
    print(level3)
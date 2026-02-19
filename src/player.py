class Bingo:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def update_score(self, points):
        self.score += points

    def get_score(self):
        return self.score

    def __str__(self):
        return f'Player: {self.name}, Score: {self.score}'
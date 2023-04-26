class LifeSystem:
    def __init__(self, max_lives=3):
        self.max_lives = max_lives
        self.remaining_lives = max_lives

    def lose_life(self):
        self.remaining_lives -= 1
        return self.remaining_lives > 0

    def reset(self):
        self.remaining_lives = self.max_lives
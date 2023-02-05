class GameStats:
    #track statistics for alien invasion

    def __init__(self,ai_game):
        #initialize statistics
        self.settings = ai_game.settings
        self.reset_stats()

        #start alien invasion in an active state
        self.game_active = True

        #high score should be reset
        self.high_score = 0

    def reset_stats(self):
        #initialize statistics that can change during thr game
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
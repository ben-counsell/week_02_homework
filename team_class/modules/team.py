class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0
    def add_player(self, new_player):
        self.players.append(new_player)
    def has_player(self, input_name):
        return input_name in self.players
    def play_game(self, win_boolean):
        if win_boolean:
            self.points += 3
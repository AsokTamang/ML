
class Player:
    def __init__(self,name,game):
        self.name=name
        self.game=game
class Basketball(Player):
    def __init__(self,name,game,mvp):
        super().__init__(name,game)
        self.mvp=mvp
    def get_mvp(self):
        return self.mvp
class Football(Player):
    def __init__(self, name, game, goldenball):
        super().__init__(name,game)
        self.goldenball=goldenball
    def get_goldenball(self):
        return self.goldenball
curry=Basketball('Curry','basketball',4)
messi = Football('Messi','football',8)
print(curry.get_mvp())
print(messi.get_goldenball())

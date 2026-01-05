class Player:
    def __init__(self,name,champs,mvps):
        self.name=name
        self.champs=champs
        self.mvps=mvps
        self.score = []
    def add_score(self,points):
        self.score.append(points)
    def calculate_avg(self):
        return sum(self.score)//len(self.score)
curry = Player('Stephen curry',4,3)
curry.add_score(44)
curry.add_score(32)
curry.add_score(56)
print(curry.calculate_avg())

lebron = Player('Lebron James',4,4)
lebron.add_score(37)
lebron.add_score(28)
lebron.add_score(55)
print(lebron.calculate_avg())



import datetime
class Player:
    def __init__(self,name,champs,mvps,dob):
        self.name=name
        self.champs=champs
        self.mvps=mvps
        self.dob=dob
        self.score = []
    def add_score(self,points):
        self.score.append(points)
    def calculate_avg(self):
        return sum(self.score)//len(self.score)
    def get_age(self):
        return datetime.datetime.now().year - self.dob
    def __lt__(self,other):
        avg_score = self.calculate_avg()
        other_score=other.calculate_avg()
        return avg_score<other_score  #here we are comparing if the current class's average score is lesser than that of other class
    def __gt__(self,other):
        avg_score = self.calculate_avg()
        other_score = other.calculate_avg()
        return avg_score > other_score  #here we are checking if the average score of this current class is greater than that of the other class or not
curry = Player('Stephen curry',4,3,1989)
curry.add_score(44)
curry.add_score(32)
curry.add_score(56)
print(curry.calculate_avg())
print(curry.get_age())
lebron = Player('Lebron James',4,4,1982)
lebron.add_score(37)
lebron.add_score(28)
lebron.add_score(55)
print(lebron.calculate_avg())
print(lebron.calculate_avg())
print(lebron<curry)


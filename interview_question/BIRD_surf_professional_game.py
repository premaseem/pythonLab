## Professional Surfing Game. Was give in Bird coding interview_question, with expectation to finish in 30 min

#  Game Rules:

# Each player would take turns and could score in scale of 0 to 10
# final score is sum of top 2 or best 2 attempts in score

# Output:
# Print the name and score of the winner

# sample
# Adam: 8, 7, 3, 8
# Aseem: 9, 1, 2, 2
# Todd: 10, 1, 1, 1


import random
class Player():

    def __init__(self, name):
        self.name = name
        self.scores = []
        self.finalScore = 0

    def calculateScore(self):
        self.scores.sort(reverse=True)
        self.finalScore = self.scores[0] + self.scores[1]
        return self.finalScore

    def take_turn(self):
        s = random.randrange(0, 10)
        self.scores.append(s)

    def __repr__(self):
        return self.name + " scored "+ str(self.finalScore)


print("Weclome to Surf game")

toppers = []

p1 = Player("Adam")
p2 = Player("Aseem")
p3 = Player("Todd")
players = [p1,p2,p3]

for _ in range(7):
    for _player in players:
        _player.take_turn()

for _player in players:
    _player.calculateScore()


players.sort(key=lambda x: x.finalScore, reverse =True)
wp = players[0]
print("winner is player", wp.name, wp.finalScore)


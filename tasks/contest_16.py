class HighScoreTable:

    def __init__(self, max_size):
        self.max_size = max_size
        self.scores = []

    def update(self, score):
        self.scores.append(score)
        self.__validator()

    def reset(self):
        self.scores.clear()

    def __validator(self):
        self.scores.sort(reverse=True)
        if len(self.scores) > self.max_size:
            self.scores.pop()


highScoreTable = HighScoreTable(3)
highScoreTable.update(10)
highScoreTable.update(8)
highScoreTable.update(30)
highScoreTable.update(20)
print(highScoreTable.scores)
highScoreTable.update(1)
highScoreTable.update(50)
print(highScoreTable.scores)

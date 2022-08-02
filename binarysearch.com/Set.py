class CustomSet:
    def __init__(self):
        self.data = {}

    def add(self, val):
        self.data[val] = 1

    def exists(self, val):
        try:
            return self.data[val] == 1
        except KeyError:
            return False

    def remove(self, val):
        self.data[val] = 0

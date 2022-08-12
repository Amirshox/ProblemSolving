class Solution:
    def solve(self, relations):
        relations = set((tuple(pair) for pair in relations))
        mutual = set()
        for x, y in relations:
            if (y, x) in relations:
                mutual.add(x)
                mutual.add(y)
        return [i for i in range(2 * len(relations) + 2) if i in mutual]

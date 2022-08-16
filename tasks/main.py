with open('input.txt') as f:
    a, b = f.readline().split()


def solution(x, y):
    bulls = 0
    cows = 0

    for i, v in enumerate(x):

        if v == y[i]:
            bulls += 1

        elif v in y:
            cows += 1

    return f"{bulls} {cows}"


with open('output.txt', 'w') as f:
    f.write(solution(a, b))

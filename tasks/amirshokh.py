# with open('input.txt') as f:
#     a, b = f.readline().split()


def a(i, j, x, y):
    if i - j == x - y:
        return 1
    i += 1
    j -= 1

    return 0

def a(i, j, x, y):
    if i - j == x - y:
        return 1
    i += 1
    j -= 1

    return 0


def solution(x: int, y: int) -> int:
    result = 0

    for i in range(1, x + 1):
        for j in range(1, y + 1):
            result += x - 1 + y - 1

            while i == x or j == 1:
                result += a(i, j, x, y)

            while i == 1 or j == y:
                result += 1
                i -= 1
                j += 1

            while i == 1 or j == 1:
                result += 1
                i -= 1
                j -= 1

            while i == x or j == y:
                result += 1
                i += 1
                j += 1

    return result


print(solution(2, 2))

# with open('output.txt', 'w') as f:
#     result = solution(int(a), int(b))
#     f.write(str(result))

# with open('input.txt') as f:
#     a, b = f.readline().split()


def solution(x: int, y: int) -> int:
    result = 0

    for i in range(1, x + 1):
        for j in range(1, y + 1):
            result += x - 1 + y - 1

            a, b = i, j
            while i <= x or j >= 1:
                if i + j == x + y:
                    result += 1
                i += 1
                j -= 1

            i, j = a, b
            while i >= 1 or j <= y:
                if i + j == x + y:
                    result += 1
                i -= 1
                j += 1

            i, j = a, b
            while i >= 1 or j >= 1:
                if i - j == x - y:
                    result += 1
                i -= 1
                j -= 1

            i, j = a, b
            while i <= x or j <= y:
                if i - j == x - y:
                    result += 1
                i += 1
                j += 1

    return result


print(solution(2, 3))

# with open('output.txt', 'w') as f:
#     result = solution(int(a), int(b))
#     f.write(str(result))

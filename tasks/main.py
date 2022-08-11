from math import lcm, gcd

with open('input.txt') as f:
    a, b = f.readline().split()
    a, b = int(a), int(b)


def custom_lcm(x, y):
    # result = lcm(x, y)

    if x % y == 0:
        return x
    if y % x == 0:
        return y

    greater = x if x > y else y

    while True:
        if greater % x == 0 and greater % y == 0:
            result = greater
            break
        greater += 1

    return result


file = open('output.txt', 'w')
file.write(str(custom_lcm(a, b)))
file.close()

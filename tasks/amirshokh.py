INT_HEX = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
}


def max_or_min(num):
    if num > 255:
        return 255
    elif num < 0:
        return 0
    return num


def int_to_hex(num):
    return INT_HEX[num // 16] + INT_HEX[num % 16]


def rgb(r, g, b):
    r = max_or_min(r)
    g = max_or_min(g)
    b = max_or_min(b)

    return int_to_hex(r) + int_to_hex(g) + int_to_hex(b)


print(rgb(255, 255, 255))

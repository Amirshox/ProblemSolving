def magic(num: int) -> int:
    dct = {
        5: 10,
        10: 5
    }
    return dct[num]


print(magic(5))
print(magic(10))

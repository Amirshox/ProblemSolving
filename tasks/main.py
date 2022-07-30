def gen():
    i = 0
    while i < 10:
        i += 1
        yield i


a = gen()
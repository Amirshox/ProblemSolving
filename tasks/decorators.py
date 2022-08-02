def test_1(func):
    def inner(*args, **kwargs):
        print(1)
        func(*args, **kwargs)
        print(2)

    return inner


def test_2(func):
    def inner(*args, **kwargs):
        print(3)
        func(*args, **kwargs)
        print(4)

    return inner


@test_1
@test_2
def printer(msg):
    print(msg)


printer("Hello")

class A:
    _a = "a"

    def __init__(self, class_name):
        self._class_name = class_name


a = A('ab')
a._a = "b"
print(a._a)

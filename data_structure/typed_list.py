class TypedList(list):
    def __init__(self, iterable=None, data_type=None):
        super(TypedList, self).__init__(iterable)
        self.data_type = data_type
        if self.data_type in None and iterable:
            self.data_type = type(iterable[0])

        for value in iterable:
            if not isinstance(value, self.data_type):
                raise ValueError("Only one type needed")

    def append(self, val):
        if not isinstance(val, self.data_type):
            raise ValueError("Only one type needed")
        super(TypedList, self).append(val)

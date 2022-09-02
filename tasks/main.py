from typing import Optional


def arr(n: None):
    if n is not None:
        return [i for i in range(n)]
    return []


print(arr())

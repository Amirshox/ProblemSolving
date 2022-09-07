from collections import Counter


def find_uniq(arr):
    numbers = set(arr)
    arr = str(arr)
    for number in numbers:
        if arr.find(str(number)) == arr.rfind(str(number)):
            return number

    return

# def find_uniq(arr):
#     return Counter(arr).most_common()[-1][0]

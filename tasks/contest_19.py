def zero_plentiful(arr):
    result, count_of_zero = 0, 0

    for elem in arr:
        if elem == 0:
            count_of_zero += 1
        else:
            if not count_of_zero < 4:
                result += 1
            elif 0 < count_of_zero < 4:
                return 0
            count_of_zero = 0
    else:
        if not count_of_zero < 4:
            result += 1
        elif 0 < count_of_zero < 4:
            return 0

    return result

def number_of_ways(n, k) -> int:
    result = 0
    if n == 1:
        return 1
    else:
        for i in range(1, k + 1):
            result += number_of_ways(n - 1, k)
    return result


print(number_of_ways(4, 3))

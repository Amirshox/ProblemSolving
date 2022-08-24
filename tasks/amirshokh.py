def fifo(n, reference_list):
    index = 0
    result = [-1] * n

    for num in reference_list:
        if num not in result:
            if index >= n:
                index = 0
            result[index] = num
            index += 1
        else:
            continue

    return result

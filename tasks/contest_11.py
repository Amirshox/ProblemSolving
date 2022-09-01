def land_perimeter(arr: list) -> int:
    length = len(arr)
    result = 0
    full_string = list(''.join(arr))
    length_full_string = len(full_string)
    print(full_string, length)

    for i, char in enumerate(full_string):
        sub_res = 1

        if char == "X":
            cur_x = i + 1
            cur_y = i + length
            full_string[i] = "O"
            while cur_x <= length_full_string and full_string[cur_x] == "X":
                sub_res += 1
                full_string[cur_x] = "O"
                cur_x += 1
                cur_y += 1
            while cur_y <= length_full_string and full_string[cur_y] == "X":
                sub_res += 1
                full_string[cur_y] = "O"
                cur_y += length
                cur_x += length
            result += sub_res * 2 + 2

    return result


print(land_perimeter(arr=['XOOXO',
                          'XOOXO',
                          'OOOXO',
                          'XXOXO',
                          'OXOOO']))

# p = n1 * 2 + 2 + n2 * 2+2
# p = (n1 + 1)*2 + (n2+1)*2
# p = 2 *(n1+ n2 + n)

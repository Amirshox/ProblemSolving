def land_perimeter(arr):
    len_arr, len_sub_arr = len(arr), len(arr[0])
    perimeter = 0
    for i in range(len_arr):
        for j in range(len_sub_arr):
            if arr[i][j] == 'X':
                perimeter += 4
                if i < len_arr - 1 and arr[i + 1][j] == 'X':
                    perimeter -= 2
                if j < len_sub_arr - 1 and arr[i][j + 1] == 'X':
                    perimeter -= 2

    return 'Total land perimeter: {}'.format(perimeter)


print(land_perimeter(arr=['XOOXO',
                          'XOOXO',
                          'OOOXO',
                          'XXOXO',
                          'OXOOO']))

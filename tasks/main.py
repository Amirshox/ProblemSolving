def combos(ls):
    if len(ls) == 1:
        return ls[0]
    else:
        ans = []
        for s1 in combos(ls[1:]):
            for s2 in ls[0]:
                ans.append(s2+s1)
        return ans

def get_pins(observed):
    could_be = {
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9'],
        '0': ['8', '0']
    }
    return combos([could_be[c] for c in observed])
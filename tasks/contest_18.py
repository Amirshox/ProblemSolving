def my_first_interpreter(code):
    i, result = 0, ''
    for ch in code:
        if ch == '+':
            i = (i + 1) % 256
        elif ch == '.':
            result += chr(i)
    return result

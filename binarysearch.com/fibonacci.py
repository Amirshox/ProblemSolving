# 0, 1, 1, 2, 3, 5, 7, 11, 13, 17, 19

def fibo(n, first_arg=10, second_arg=7):
    if n == 1:
        return first_arg
    if n == 2:
        return second_arg
    else:
        return fibo(n - 1) + fibo(n - 2)


num = int(input("Input number: "))

print(fibo(num))

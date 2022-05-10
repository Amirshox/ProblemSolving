def chain_sum(number):
    result = number

    def wrapper(number2=None):
        nonlocal result
        if number2 is None:
            return result
        result += number2
        return wrapper

    return wrapper


print(chain_sum(5)())
print(chain_sum(5)(10)())
print(chain_sum(5)(2)(3)())

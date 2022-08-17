with open('input.txt') as f:
    numbers = f.readline().split()
    numbers = [int(number) for number in numbers]


def solution(nums: list) -> str:
    is_increased = True if nums[0] < nums[1] else False
    sawtooth_count = max_sawtooth_count = 2

    for i in range(2, len(nums)):
        if is_increased:
            if nums[i - 1] > nums[i]:
                sawtooth_count += 1
                is_increased = False
            else:
                if max_sawtooth_count < sawtooth_count:
                    max_sawtooth_count = sawtooth_count
                sawtooth_count = 2
                is_increased = True
        else:
            if nums[i - 1] < nums[i]:
                sawtooth_count += 1
                is_increased = True
            else:
                if max_sawtooth_count < sawtooth_count:
                    max_sawtooth_count = sawtooth_count
                sawtooth_count = 2
                is_increased = False

    return str(max_sawtooth_count if max_sawtooth_count > sawtooth_count else sawtooth_count)


with open('output.txt', 'w') as f:
    f.write(solution(numbers))

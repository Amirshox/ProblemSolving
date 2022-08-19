letter_string = 'abcdefghijklmnopqrstuvwxyz'
letters = [
    'aa',
    'ab',
    'ac',
    'ad',
    'ae',
    'af',
    'ag',
    'ah',
    'ai',
    'aj',
    'ak',
    'al',
    'am',
    'an',
    'ao',
    'ap',
    'aq',
    'ar',
    'as',
    'at',
    'au',
    'av',
    'aw',
    'ax',
    'ay',
    'az',
]

full_letters = []

for letter in letters:

    for second_index in list(range(1, 26)):

        for index in list(range(0, 26)):
            full_letters.append(letter_string[index] + letter)

        letter = letter_string[second_index] + letter[-1]

    for index in list(range(0, 26)):
        full_letters.append(letter_string[index] + letter_string[-1] + letter[-1])
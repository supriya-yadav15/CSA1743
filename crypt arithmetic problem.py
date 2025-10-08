from itertools import permutations

def solve_cryptarithmetic(puzzle):
    parts = puzzle.replace(' ', '').split('=')
    left_side, result_word = parts
    words = left_side.split('+')
    letters = set(''.join(words + [result_word]))
    if len(letters) > 10:
        return None
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if any(mapping[word[0]] == 0 for word in words + [result_word]):
            continue
        word_values = [int(''.join(str(mapping[l]) for l in word)) for word in words]
        result_value = int(''.join(str(mapping[l]) for l in result_word))
        if sum(word_values) == result_value:
            return mapping
    return None

puzzle = "SEND + MORE = MONEY"
mapping = solve_cryptarithmetic(puzzle)
if mapping:
    print(mapping)
    translated = puzzle
    for letter, digit in mapping.items():
        translated = translated.replace(letter, str(digit))
    print(translated)
else:
    print('No solution found.')

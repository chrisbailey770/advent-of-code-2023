### PART 2 STILL UNSOLVED ###

import re
from collections import defaultdict

SYMBOL_PATTERN = re.compile('[@_!$%^&*()<>?/|}{~:#+=-]')
ASTERISK = re.compile('[*]')

def adjacent_to_symbol(sample_input, row, col):
    # check above if not the first row
    if row != 0:
        if bool(re.match(SYMBOL_PATTERN, sample_input[row-1][col])):
            return True
    # check below if not the last row
    if row != len(sample_input)-1:
        if bool(re.match(SYMBOL_PATTERN, sample_input[row+1][col])):
            return True
    # check left if not the first column
    if col != 0:
        if bool(re.match(SYMBOL_PATTERN, sample_input[row][col-1])):
            return True
    # check right if not the last column
    if col != len(sample_input[row])-1:
        if bool(re.match(SYMBOL_PATTERN, sample_input[row][col+1])):
            return True
    # check upper left if not first row and not first column
    if row != 0 and col != 0:
        if bool(re.match(SYMBOL_PATTERN, sample_input[row-1][col-1])):
            return True
    # check upper right if not first row and not last column
    if row != 0 and col != len(sample_input[row])-1:
        if bool(re.match(SYMBOL_PATTERN, sample_input[row-1][col+1])):
            return True
    # check lower left if not last row and not first column
    if row != len(sample_input)-1 and col != 0:
        if bool(re.match(SYMBOL_PATTERN, sample_input[row+1][col-1])):
            return True
    # check lower right if not last row and not last column
    if row != len(sample_input)-1 and col != len(sample_input[row]):
        if bool(re.match(SYMBOL_PATTERN, sample_input[row+1][col+1])):
            return True
    return False

def adjacent_to_gear(sample_input, row, col):
    # check above if not the first row
    if row != 0:
        if bool(re.match(ASTERISK, sample_input[row-1][col])):
            return True, row-1, col
    # check below if not the last row
    if row != len(sample_input)-1:
        if bool(re.match(ASTERISK, sample_input[row+1][col])):
            return True, row+1, col
    # check left if not the first column
    if col != 0:
        if bool(re.match(ASTERISK, sample_input[row][col-1])):
            return True, row, col-1
    # check right if not the last column
    if col != len(sample_input[row])-1:
        if bool(re.match(ASTERISK, sample_input[row][col+1])):
            return True, row, col+1
    # check upper left if not first row and not first column
    if row != 0 and col != 0:
        if bool(re.match(ASTERISK, sample_input[row-1][col-1])):
            return True, row-1, col-1
    # check upper right if not first row and not last column
    if row != 0 and col != len(sample_input[row])-1:
        if bool(re.match(ASTERISK, sample_input[row-1][col+1])):
            return True, row-1, col+1
    # check lower left if not last row and not first column
    if row != len(sample_input)-1 and col != 0:
        if bool(re.match(ASTERISK, sample_input[row+1][col-1])):
            return True, row+1, col-1
    # check lower right if not last row and not last column
    if row != len(sample_input)-1 and col != len(sample_input[row]):
        if bool(re.match(ASTERISK, sample_input[row+1][col+1])):
            return True, row+1, col+1
    return False, None, None

if __name__ == "__main__":

    with open('input.txt') as f:
        schematic = f.readlines()

    nums_1 = []
    nums_2 = defaultdict(list)
    sum_2 = 0
    gears = set()
    adjacency_flag = False
    gear_flag = False
    num_string = ""
    for row, line in enumerate(schematic):
        for col, char in enumerate(line):
            if char.isnumeric():
                num_string += char
                if adjacent_to_symbol(schematic, row, col):
                    adjacency_flag = True
                gear_bool, gear_row, gear_col = adjacent_to_gear(schematic, row, col)
                if gear_bool:
                    gear_flag = True
                    gears.add((row, col))
            if not char.isnumeric():
                if adjacency_flag:
                    if len(num_string) > 0:
                        num = int(num_string)
                        nums_1.append(num)
                        num_string = ""
                        adjacency_flag = False
                else:
                    num_string = ""
                    num = []

    for gear in gears:
        print(gear)
        nums_2[gear].append(schematic[gear[0]][gear[1]])

print(nums_1)
print(f'Part 1 sum is {sum(nums_1)}')

print(nums_2)

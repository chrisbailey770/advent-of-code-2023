from typing import List
import re


def get_nums_from_line(line: str) -> List[int]:
    nums = []
    for char in line:
        if char.isnumeric():
            nums.append(int(char))
    return nums


def get_first_and_last_num(nums: List[int]) -> int:
    first = str(nums[0])
    last = str(nums[-1])
    num = int("".join([first, last]))
    return num


def replace_words(line: str) -> str:

    map = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': 'f4r',
        'five': 'f5e',
        'six': 's6x',
        'seven': 's7n',
        'eight': 'e8t',
        'nine': 'n9e',
        'zero': 'z0o'
    }

    for k, v in map.items():
        line = line.replace(k, v)
    return line


if __name__ == '__main__':

    with open('input.txt') as f:
        data = f.readlines()

    # part 1
    sum = 0

    for line in data:
        nums = get_nums_from_line(line)
        num = get_first_and_last_num(nums)
        sum += num

    print(f'Part 1 Sum: {sum}')

    # part 2
    sum = 0

    for line in data:
        line = replace_words(line)
        nums = get_nums_from_line(line)
        num = get_first_and_last_num(nums)
        sum += num

    print(f'Part 2 Sum: {sum}')
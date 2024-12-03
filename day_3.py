### https://adventofcode.com/2024

import re


DAY = 3


def read_file(file_name):
    with open(file_name, 'r') as f_in:
        return str(list(filter(None, [line.strip() for line in f_in.readlines()])))


def get_solution_1(_data):
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    res = re.findall(pattern, _data)
    res = [re.findall(r'\d+', item) for item in res]
    return sum([int(num1) * int(num2) for (num1, num2) in res])
        
    
def get_solution_2(data):
    res = 0
    instructions = str(data).split("don't()")
    if not data.startswith("don't()"):
        start = instructions[0]
    instructions = [start] + list(filter(None, [item.split("do()")[1:] for item in instructions]))
    for item in instructions:
        res += get_solution_1(str(item))
    return res




file = f"../data/day_{DAY}.txt"


data = read_file(file)

solution_1 = get_solution_1(data)
solution_2 = get_solution_2(data)

print(f"Day {DAY} - Solution 1:", solution_1)
print(f"Day {DAY} - Solution 2:", solution_2)

# Day 3 - Solution 1: 184511516
# Day 3 - Solution 2: 90044227
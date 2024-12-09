### https://adventofcode.com/2024

import time
import itertools

DAY = 7


def read_file(file_name):
    with open(file_name, 'r') as f_in:
        return list(filter(None, [line.strip() for line in f_in.readlines()]))
    
    
def parse_input(_data):
    parsed_data = []
    for item in _data:
        res, ops = item.split(': ')
        res, ops = int(res), ops.split(' ')
        parsed_data.append({"res": res, "ops": ops})
    return parsed_data

    

def get_solution_1(_data):
    sum_valid = 0
    for item in _data:
        res = item["res"]
        ops = item["ops"]
        num_ops = len(ops) - 1  
        patterns = itertools.product([' + ', ' * '], repeat=num_ops)
        for pattern in patterns:
            pattern = (" + ", *pattern)
            result = '0'
            for idx, op in enumerate(pattern):
                result = eval(str(result) + op + ops[idx])
            if result == res:
                sum_valid += res
                break            
    return sum_valid

    
def get_solution_2(_data):
    sum_valid = 0
    for item in _data:
        res = item["res"]
        ops = item["ops"]
        num_ops = len(ops) - 1  
        patterns = itertools.product(['+', '*', '||'], repeat=num_ops)
        for pattern in patterns:
            pattern = (" + ", *pattern)
            result = '0'
            for idx, op in enumerate(pattern):
                operand = ops[idx]
                if op == '||':
                    result = str(result) + ops[idx]                    
                else:
                    result = eval(str(result) + op + ops[idx])
            if int(result) == res:
                sum_valid += res
                break            
    return sum_valid



start = time.time()
file = f"../data/day_{DAY}.txt"


data = read_file(file)
data = parse_input(data)
# print(data)

solution_1 = get_solution_1(data)
solution_2 = get_solution_2(data)

print(f"Day {DAY} - Solution 1:", solution_1)
print(f"Day {DAY} - Solution 2:", solution_2)
print(f"Execution time: {time.time() - start} seconds")

# Day 7 - Solution 1: 4122618559853
# Day 7 - Solution 2: 227615740238334
 

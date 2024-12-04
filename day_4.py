### https://adventofcode.com/2024

import numpy as np


DAY = 4


def read_file(file_name):
    with open(file_name, 'r') as f_in:
        return list(filter(None, [line.strip() for line in f_in.readlines()]))


def get_sum_horizontal(_data, search):
    rev_search = search[::-1]
    fwd = sum([line.count(search) for line in _data])
    rev = sum([line.count(rev_search) for line in _data])
    return fwd + rev

    
def get_sum_vertical(_data, search):
    rev_search = search[::-1]
    fwd, rev = 0, 0
    for j in range(len(_data[0])):
        fwd  += ''.join([_data[i][j] for i in range(len(_data))]).count(search)
        rev  += ''.join([_data[i][j] for i in range(len(_data))]).count(rev_search)
    return fwd + rev
    
    
def get_sum_diagonals(arr, search, num_cols, num_rows):
    rev_search = search[::-1]        
    sum_diag = 0
    
    # central diagonal (k=0) and
    # diagonals located upper and right from the central diagonal
    for j in range(num_cols):
        d = ''.join(np.diag(arr, k=j))
        sum_diag += d.count(search)      # fwd
        sum_diag += d.count(rev_search)  # rev
    
    # no central diagonal (k!=0)
    # diagnoals located lower left from the central diagonal
    for i in range(1, num_rows):
        d = ''.join(np.diag(arr, k=-1*i))
        sum_diag += d.count(search)      # fwd
        sum_diag += d.count(rev_search)  # rev
    return sum_diag


def get_solution_1(_data, search):
    total_sum = get_sum_horizontal(_data, search)
    total_sum += get_sum_vertical(_data, search)
    
    num_cols = len(_data[0])
    num_rows = len(_data)
    
    # for diagonals from top left to bottom right
    arr = np.array([list(item) for item in _data])
    total_sum += get_sum_diagonals(arr, search, num_cols, num_rows)
    
    # for diagonals from bottom left to top right
    arr_flip = np.fliplr(arr)
    total_sum += get_sum_diagonals(arr_flip, search, num_cols, num_rows)
    return total_sum
        
    
def get_solution_2(_data):
    num_cols = len(_data[0])
    num_rows = len(_data)
    total_sum = 0
    allowed_patterns = [
        "MMSS", "MSMS", "SSMM", "SMSM" 
    ]
    for j in range(1, num_cols - 1):
        for i in range(1, num_rows - 1):
            if _data[i][j] == "A":
                pattern = ''.join([
                    _data[i - 1][j - 1], 
                    _data[i - 1][j + 1],
                    _data[i + 1][j - 1], 
                    _data[i + 1][j + 1]
                ])
                total_sum += 1 if pattern in allowed_patterns else 0
    return total_sum
                            


    
file = f"../data/day_{DAY}.txt"

search_item = "XMAS"

data = read_file(file)

solution_1 = get_solution_1(data, search_item)
solution_2 = get_solution_2(data)

print(f"Day {DAY} - Solution 1:", solution_1)
print(f"Day {DAY} - Solution 2:", solution_2)

# Day 4 - Solution 1: 2434
# Day 4 - Solution 2: 1835
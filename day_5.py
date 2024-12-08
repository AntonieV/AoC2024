### https://adventofcode.com/2024

import json


DAY = 5


def read_file(file_name):
    with open(file_name, 'r') as f_in:
        return list(filter(None, [line.strip() for line in f_in.readlines()]))
    
def parse_input(_data):
    paths = []
    upstream = dict()
    downstream = dict()
    for item in data:
        if "|" in item:
            v1, v2 = item.split("|")
            if v1 not in upstream:
                upstream[v1] = []
            upstream[v1].append(v2)
            
            if v2 not in downstream:
                downstream[v2] = []
            downstream[v2].append(v1)
        if "," in item:
            paths.append(item.split(","))
    return upstream, downstream, paths


def is_valid(_up, _down, path, idx):
    list_down = path[:idx]
    list_up = path[idx + 1:]
    for item in list_up:
        if path[idx] not in _up or item not in _up[path[idx]]:
            return False
    for item in list_down:
        if path[idx] not in _down or item not in _down[path[idx]]:
            return False
    return True


def get_solution_1(_up, _down, paths):
    incorrect_updates = []
    sum_middle_elem = 0
    for path in paths:
        valid_items = []
        for idx, item in enumerate(path):
            valid_items.append(is_valid(_up, _down, path, idx))
        if all(valid_items):
            sum_middle_elem += int(path[len(path)//2])
            continue
        incorrect_updates.append(path)            
    return sum_middle_elem, incorrect_updates

   
def swap_order(order, idx_curr, current, idx_prev, prev):
    order[idx_prev] = current
    order[idx_curr] = prev
    return order
    
    
def get_order(_up, _down, path):
    order = []
    for idx, current in enumerate(path):
        order.append(current)
        for prev in path[:idx]:  
            idx_curr = order.index(current)
            idx_prev = order.index(prev)
            if current in _up and prev in _up[current]:    
                if idx_curr > idx_prev:
                    order = swap_order(order, idx_curr, current, idx_prev, prev)                    
            elif current in _down and prev in _down[current]:
                if idx_curr < idx_prev:
                    order = swap_order(order, idx_curr, current, idx_prev, prev)
    _, incorrect = get_solution_1(_up, _down, [order])
    if incorrect != []:
        order = get_order(_up, _down, order)
        
    return order
        
    
def get_solution_2(_up, _down, paths):
    sum_middle_elem = 0
    for path in paths:
        fixed_path = get_order(_up, _down, path)        
        sum_middle_elem += int(fixed_path[len(fixed_path)//2])
    return sum_middle_elem


        


file = f"../data/day_{DAY}.txt"

data = read_file(file)
up, down, _paths = parse_input(data)


solution_1, incorrect = get_solution_1(up, down, _paths)
solution_2 = get_solution_2(up, down, incorrect)

print(f"Day {DAY} - Solution 1:", solution_1)
print(f"Day {DAY} - Solution 2:", solution_2)

# Day 5 - Solution 1: 5268
# Day 5 - Solution 2: 5799
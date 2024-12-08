 
### https://adventofcode.com/2024

DAY = 6

DIRECTION_SWITCH_MAP = {
    "up": "right",
    "down": "left",
    "left": "up",
    "right": "down",
}

def read_file(file_name):
    with open(file_name, 'r') as f_in:
        return list(filter(None, [line.strip() for line in f_in.readlines()]))
    
    
def get_start_idx(_data):
    start = ''.join(_data).index('^')
    i_row = start // len(_data)
    i_col = start % len(_data[0])    
    return i_row, i_col


def get_next_position(direction, curr_row, curr_col):
    if direction == "up":     
        next_row = curr_row - 1
        next_col = curr_col        
    elif direction == "down":
        next_row = curr_row + 1
        next_col = curr_col
    elif direction == "left":
        next_row = curr_row 
        next_col = curr_col - 1
    elif direction == "right":
        next_row = curr_row
        next_col = curr_col + 1
    return next_row, next_col


def get_next(_data, direction, curr_row, curr_col):
    num_rows = len(_data[curr_row])
    num_cols = len(_data)
    next_row, next_col = get_next_position(direction, curr_row, curr_col)    
    _data[curr_row] = _data[curr_row][:curr_col] + 'X' + _data[curr_row][(curr_col + 1):]
    if next_row < 0 or next_row >= num_rows or next_col < 0 or next_col >= num_cols:
        return False, _data, curr_row, curr_col, direction
    _next = _data[next_row][next_col]
    
    while _next == "#":
        direction = DIRECTION_SWITCH_MAP[direction]
        return get_next(_data, direction, curr_row, curr_col)
    
    return True, _data, next_row, next_col, direction


def get_solution_1(_data):
    curr_row, curr_col = get_start_idx(_data)
    direction = "up"
    while True:
        has_next, _data, curr_row, curr_col, direction = get_next(_data, direction, curr_row, curr_col)
        if not has_next:
            break  
    return ''.join(_data).count("X"), _data
            
    
def get_all_possibile_positions(_data):
    positions = []
    for row, line in enumerate(_data):
        for col, char in enumerate(line):
            if char == 'X':
                positions.append([row, col])
    return positions
    

def get_next_in_cycle(_data, direction, curr_row, curr_col, row, col, cnts, positions):
    num_rows = len(_data[curr_row])
    num_cols = len(_data)
    next_row, next_col = get_next_position(direction, curr_row, curr_col)  
    
    if [next_row, next_col] in positions:
        cnts += 1
    if cnts > 10000:  # is cycle
        return True, _data, next_row, next_col, direction, True, cnts
        
    if next_row < 0 or next_row >= num_rows or next_col < 0 or next_col >= num_cols:
        return False, _data, curr_row, curr_col, direction, False, cnts
    _next = _data[next_row][next_col]
    
    while _next == "#" or _next == "O":
        direction = DIRECTION_SWITCH_MAP[direction]
        return get_next_in_cycle(_data, direction, curr_row, curr_col, row, col, cnts, positions)
    return True, _data, next_row, next_col, direction, False, cnts
    
    
def get_solution_2(_data, s_row, s_col):
    possibilities = set()
    positions = get_all_possibile_positions(_data)
    for row, col in positions:
        curr_data = [x[:] for x in _data]
        if row == s_row and col == s_col:
            continue
        curr_data[row] = curr_data[row][:col] + 'O' + curr_data[row][(col + 1):]
        
        cnts = 0
        direction = "up"
        curr_row, curr_col = s_row, s_col
        while True:
            has_next, curr_data, curr_row, \
            curr_col, direction, has_loop, cnts = get_next_in_cycle(curr_data, 
                                                              direction, 
                                                              curr_row, 
                                                              curr_col, 
                                                              row,
                                                              col,
                                                              cnts,
                                                              positions
                                                             )
            if not has_next:
                break 
            if has_loop:
                possibilities.add(f"{row}_{col}")
                break
    return len(possibilities)

        


file = f"../data/day_{DAY}.txt"

data = read_file(file)
start_row, start_col = get_start_idx(data)

solution_1, final = get_solution_1(data)
# for line in final + ["\n"]:
#     print(line)
print(f"Day {DAY} - Solution 1:", solution_1)

# look at each position which the guard visits, store the previous position
# change it to 'O' or '#' and check if the guard visits the previous position again
# if it visits again -> possible position += 1

solution_2 = get_solution_2(final, start_row, start_col)
print(f"Day {DAY} - Solution 2:", solution_2)

# Day 6 - Solution 1: 4663
# Day 6 - Solution 2: 1530

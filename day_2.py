### https://adventofcode.com/2024

DAY = 2


def read_file(file_name):
    with open(file_name, 'r') as f_in:
        return list(filter(None, [line.strip().split(' ') for line in f_in.readlines()]))

        
def is_decreasing(report):
    curr = report[0]
    for i in range(len(report) - 1):
        _next = report[i + 1]
        low, high = curr - 3, curr - 1
        if low > _next or high < _next:
            return False
        curr = report[i + 1]
    return True


def is_increasing(report):
    curr = report[0]
    for i in range(len(report) - 1):
        _next = report[i + 1]
        low, high = curr + 1, curr + 3   
        if low > _next or high < _next:
            return False
        curr = report[i + 1]
    return True
    

def get_solution_1(reports):        
    num_save = 0
    for report in reports:
        report = [int(item) for item in report]
        if is_decreasing(report) or is_increasing(report):
            num_save += 1
    return num_save
            
    
def get_solution_2(reports):
    num_save = 0
    for report in reports:
        report = [int(item) for item in report]
        tests = []
        for i in range(len(report)):
            tests.append(report[:i] + report[i + 1:])
        for test in tests:
            if is_decreasing(test) or is_increasing(test):
                num_save += 1
                break
    return num_save




file = f"../data/day_{DAY}.txt"


data = read_file(file)

solution_1 = get_solution_1(data)
solution_2 = get_solution_2(data)

print(f"Day {DAY} - Solution 1:", solution_1)
print(f"Day {DAY} - Solution 2:", solution_2)

# Day 2 - Solution 1: 282
# Day 2 - Solution 2: 349
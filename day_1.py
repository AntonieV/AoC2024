### https://adventofcode.com/2024

import re
import pandas as pd


DAY = 1

def read_and_parse(file_name):
    df = pd.read_csv(file_name, sep='\s+', header=None)
    return sorted(list(df.iloc[:, 0])), sorted(list(df.iloc[:, 1]))
    

def get_solution_1(list1, list2):
    return sum([abs(list1[i] - list2[i]) for i in range(len(list1))])
        
    
def get_solution_2(list1, list2):
    items = list(set(list1))
    return sum([item * list2.count(item) for item in items])



file = f"data/day_{DAY}.txt"


list_1, list_2 = read_and_parse(file)

solution_1 = get_solution_1(list_1, list_2)
solution_2 = get_solution_2(list_1, list_2)

print(f"Day {DAY} - Solution 1:", solution_1)
print(f"Day {DAY} - Solution 2:", solution_2) 

# Day 1 - Solution 1: 936063
# Day 1 - Solution 2: 23150395
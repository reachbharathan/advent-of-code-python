# with open("/Users/Bharathan/projects/python_practise/advent_of_code/03_input.txt", "r") as file:
import re
from collections import defaultdict

with open("/Users/Bharathan/projects/python_practise/advent_of_code/03_input.txt", "r") as file:
    input1  = list(filter(None, file.read().splitlines()))

print(input1)


#algorithm
# sample - #1 @ 1,3: 4x4
#split the input and assign the values to object
#set values for each location of the data in the entire square
#have it in a dictionary for each location and increase the count for each data
#extract the location which has more and have it in a counter
#return the counter

two_dimension_array = [[0 for x in range(1000)] for y in range(1000)]

class ClaimDetails() :
    def __init__(self, str=""):
        x = re.search("#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)", str)
        self.claim_number = int(x.group(1))
        self.left_width = int(x.group(2))
        self.top_height = int(x.group(3))
        self.rectangle_width = int(x.group(4))
        self.rectangle_height = int(x.group(5))



claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), input1)
print("claims")
print(claims)

val_tracking = defaultdict(list)
for string in input1:
    claim = ClaimDetails(string)
    for x in range(claim.top_height,claim.top_height+claim.rectangle_height):
        for y in range(claim.left_width,claim.left_width+claim.rectangle_width):
            two_dimension_array[x][y] += 1

print(two_dimension_array)
print("val+tracking")
print(val_tracking)

overlap_square = 0
for x in range(len(two_dimension_array)):
    for y in range(len(two_dimension_array)):
        if two_dimension_array[x][y] > 1:
            overlap_square += 1
print("overlap_square")
print(overlap_square)

non_overlap_square = 0
for x in range(len(two_dimension_array)):
    for y in range(len(two_dimension_array)):
        if two_dimension_array[x][y] == 1:
            non_overlap_square += 1
print(non_overlap_square)

intact_claim_number = 0
for x in range(len(two_dimension_array)):
    for y in range(len(two_dimension_array)):
        if two_dimension_array[x][y] > 1:
            overlap_square += 1
print(overlap_square)

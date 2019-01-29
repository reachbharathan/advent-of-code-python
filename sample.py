import re

# Return a list containing every occurrence of "ai":
from collections import defaultdict

from pip._vendor.msgpack.fallback import xrange

with open("/Users/Bharathan/projects/python_practise/advent_of_code/03_sample_input.txt", "r") as file:
    input1 = list(filter(None, file.read().splitlines()))


def initialize_twodlist(foo):
    twod_list = []
    new = []
    for i in range(0, 10):
        for j in range(0, 10):
            new.append(foo)
        twod_list.append(new)
        new = []
    print(twod_list)


print(initialize_twodlist("a"))

name = "1234567"
print(list(map(lambda c: int(c), name)))

claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), input1)
print("claims")
print(claims)

claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), input1)
m = defaultdict(list)
overlaps = {}
for (claim_number, start_x, start_y, width, height) in claims:
    overlaps[claim_number] = set()
    for i in xrange(start_x, start_x + width):
        for j in xrange(start_y, start_y + height):
            if m[(i, j)]:
                for number in m[(i, j)]:
                    overlaps[number].add(claim_number)
                    overlaps[claim_number].add(number)
            m[(i, j)].append(claim_number)

print("a", len([k for k in m if len(m[k]) > 1]))
print("b", [k for k in overlaps if len(overlaps[k]) == 0][0])

from collections import defaultdict

# 1373 @ 130,274: 15x26
C = defaultdict(int)
for line in input1:
    words = line.split()
    x, y = words[2].split(',')
    x, y = int(x), int(y[:-1])
    w, h = words[3].split('x')
    w, h = int(w), int(h)
    for dx in range(w):
        for dy in range(h):
            C[(x + dx, y + dy)] += 1
for line in input1:
    words = line.split()
    x, y = words[2].split(',')
    x, y = int(x), int(y[:-1])
    w, h = words[3].split('x')
    w, h = int(w), int(h)
    ok = True
    for dx in range(w):
        for dy in range(h):
            if C[(x + dx, y + dy)] > 1:
                ok = False
    if ok:
        print(words[0])


ans = 0
for (r, c), v in C.items():
    if v >= 2:
        ans += 1
print(ans)

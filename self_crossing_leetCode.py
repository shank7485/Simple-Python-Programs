"""
LeetCode
335. Self Crossing
┌───┐
│   │
└───┼──>
    │
"""

input = [2, 1, 1, 2]

flag = False

for i in range(0, (len(input) / 2)):
    if input[i] >= input[i + 2]:
        flag = True

if flag:
    print "true (self crossing)"
else:
    print "false (not self crossing)"

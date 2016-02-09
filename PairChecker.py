"""
HackerRank Interview
"""

lst = raw_input()

lst = lst.split(", ")

initial = 0

for i in lst:
    initial = int(i) ^ initial

"""
Idea is XOR of a number with itself is 0. So if I XOR all elements, it will turnup to 0 if all are pairs.
Else, it will return the number which is without a pair.
"""

print initial

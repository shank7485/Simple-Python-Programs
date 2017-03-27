"""
HackerRank: Algorithms::Strings::Alternating Characters
"""

input = int(raw_input())

for i in range(0, input):
    in_string = raw_input()
    count = 0
    prev = ""
    for i in range(0, len(in_string)):
        if prev == in_string[i]:
            count = count + 1
        prev = in_string[i]
    print count

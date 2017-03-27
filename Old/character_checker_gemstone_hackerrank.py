"""
HackerRank: Algorithms::Strings::Gemstones
"""

N = int(raw_input())

count = 0
lst = [0] * 26

for ints in range(0, N):

    input = raw_input()

    temp = []
    for chr in input:
        if chr not in temp:
            temp.append(chr)
    input = "".join(temp)

    for i in range(0, len(input)):
        char_index = ord(input[i]) - ord('a')
        lst[char_index] += 1

for i in range(0, len(input)):
    if lst[i] == N:
        count += 1

print count

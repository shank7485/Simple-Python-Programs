"""
HackerRank:  Algorithms::Implementation::Service Lane
"""


input = raw_input()
input = input.split(" ")

array_size = int(input[0])
test_cases = int(input[1])

width_array = raw_input()
width_array = width_array.split(" ")

for x in range(0, test_cases):
    minimum = 9999
    array_range = raw_input()
    array_range = array_range.split(" ")
    i = int(array_range[0])
    j = int(array_range[1])

    for q in range(i, j + 1):
        if int(width_array[q]) < minimum:
            minimum = int(width_array[q])

    print minimum

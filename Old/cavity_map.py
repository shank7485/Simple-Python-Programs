"""
HackerRank: 
 Algorithms::Implementation::Cavity Map
"""

def cavity_indicator(n, matrix):
    tracker = []
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if matrix[i][j] >= matrix[i][j - 1] and \
                matrix[i][j] >= matrix[i - 1][j] and \
                matrix[i][j] >= matrix[i + 1][j] and \
                matrix[i][j] >= matrix[i][j + 1]:
                    tracker.append((i,j))

    for tuple in tracker:
        i, j = tuple[0], tuple[1]
        matrix[i][j] = "X"

    for i in matrix:
        output = ""
        for j in i:
            output = output + str(j)
        print output

matrix2 = []

value = int(raw_input())

for i in range(0, value):
    string = raw_input()
    lst = []
    for j in string:
        number = int(j)
        lst.append(number)
    matrix2.append(lst)

cavity_indicator(value, matrix2)

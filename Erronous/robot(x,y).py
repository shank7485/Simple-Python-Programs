def func(X, Y, matrix):
    if X == 0 and Y == 0:
        return 1
    elif X == 0 and Y != 0:
        if matrix[X, Y - 1] != 0:
            return matrix[X, Y - 1]
        else:
            matrix[X, Y - 1] = func(X, Y - 1, matrix)
            return matrix[X, Y - 1]
    elif X != 0 and Y == 0:
        if matrix[X - 1, Y] != 0:
            return matrix[X - 1, Y]
        else:
            matrix[X - 1, Y] = func(X - 1, Y, matrix)
            return matrix[X - 1, Y]
    else:
        matrix[X, Y] = int(func(X - 1, Y, matrix)) + int(func(X, Y - 1, matrix))
        return matrix[X, Y]

matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

print func(2,2,matrix)
def search_in_matrix(matrix, target):

    for index, row in enumerate(matrix):
        for column, value in enumerate(row):
            if value == target:
                result = [index, column]
                return result

    return [-1, -1]


print(search_in_matrix([
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004]
    ], 44))

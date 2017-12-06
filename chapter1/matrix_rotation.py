# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)
# (2,0) (2,1) (2,2)
#
# (x,y) -> (1-y+1,x) -> (1-x+1, 1-y+1) -> (y, 1-x+1)
# (0,0) -> (2,0) -> (2,2) -> (0,2)


def rotate_m(mat):
    row = len(mat[0])
    column = len(mat)

    row_range = row//2
    col_range = column//2 if column % 2 == 0 else column//2+1
    column_idx = len(mat)-2

    for i in range(row_range):
        for j in range(col_range):
            mat[i][j], mat[column_idx-j+1][i], mat[column_idx-i+1][column_idx-j+1], mat[j][column_idx-i+1] = \
                mat[j][column_idx-i+1], mat[i][j], mat[column_idx-j+1][i], mat[column_idx-i+1][column_idx-j+1]
    return mat


if __name__ == '__main__':
    mat = [[0 for _ in range(10)] for _ in range(10)]
    row = len(mat[0])
    column = len(mat)
    for i in range(row):
        for j in range(column):
            mat[i][j] = (i, j)
    print("Before rotation", end="\n")
    for i in range(row):
        for j in range(column):
            print(mat[i][j], end=", ")
        print(end="\n")
    rotated_mat = rotate_m(mat)
    print("After rotation", end="\n")
    for i in range(row):
        for j in range(column):
            print(rotated_mat[i][j], end=", ")
        print(end="\n")

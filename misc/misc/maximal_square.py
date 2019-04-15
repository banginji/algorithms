def maximal_square(matrix):
    d = 0
    m, n = len(matrix), len(matrix[0])
    f = [[0 for _ in range(n)] for _ in range(m)]
    for idx_col in range(m):
        for idx_row in range(n):
            if idx_col == 0 or idx_row == 0:
                f[idx_col][idx_row] = matrix[idx_col][idx_row]
            elif matrix[idx_col][idx_row] == 1:
                f[idx_col][idx_row] = min(f[idx_col-1][idx_row], f[idx_col][idx_row-1], f[idx_col-1][idx_row-1]) + 1
            d = max(d, f[idx_col][idx_row])
    print(f)
    return d ** 2



def maximal_square_impl(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix:
        return 0
    d = 0
    m, n = len(matrix), len(matrix[0])
    f = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                f[i][j] = matrix[i][j]
            elif matrix[i][j] == 1:
                f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1
            d = max(d, f[i][j])
    print(f)
    return d ** 2


def create_matrix():
    return [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0]
    ]


if __name__ == '__main__':
    print('Maximal Square Impl')
    print(maximal_square(create_matrix()))

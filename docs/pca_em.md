<a href="https://colab.research.google.com/github/savioursho/data-analysis/blob/main/pca_em.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

``` python
import numpy as np
```

``` python
# 元の行列
missing_matrix = np.array(
    [[1, 2],
     [2, np.nan]]
)
missing_matrix
```

    array([[ 1.,  2.],
           [ 2., nan]])

``` python
# 欠損値があるところのマスク
mask = np.isnan(missing_matrix)
mask
```

    array([[False, False],
           [False,  True]])

``` python
# 列の平均で欠損を埋める
initialized_matrix = missing_matrix.copy()
initialized_matrix[1, 1] = 2
last_projection = initialized_matrix
initialized_matrix
```

    array([[1., 2.],
           [2., 2.]])

``` python
```

    array([[-2.19182309],
           [-2.80723529]])

``` python
def iteration(matrix, projection, mask, rank):
    last_projection = projection.copy()

    # 低ランクの行列に分解して再構成する
    u, s, vh = np.linalg.svd(matrix)
    projection = (u @ np.diag(s))[:, :rank] @ vh[:rank, :]

    # 欠損値部分を置き換え
    matrix[mask] = projection[mask]

    # 欠損部分の差を計算
    delta = last_projection[mask] - projection[mask]
    diff = np.square(delta).sum() / np.square(projection[mask]).sum()

    return matrix, projection, diff
```

``` python
matrix = np.array(
    [[1, 2, 3],
     [2, 4, 6],
     [3, 6, 100]]
)
projection = matrix.copy()
mask = np.array(
    [[False, False, False],
     [False, False, False],
     [False, False, True],]
)
for i in range(200):
    matrix, projection, diff = iteration(matrix, projection, mask, rank=1)
    if i % 20 == 0:
        print("iter:\t", i)
        print("diff:\t", diff)
        print("matrix:\t\n", matrix)
```

    iter:    0
    diff:    4.9520699503408824e-08
    matrix: 
     [[ 1  2  3]
     [ 2  4  6]
     [ 3  6 99]]
    iter:    20
    diff:    0.00015664125289152923
    matrix: 
     [[ 1  2  3]
     [ 2  4  6]
     [ 3  6 79]]
    iter:    40
    diff:    0.00027935416986875144
    matrix: 
     [[ 1  2  3]
     [ 2  4  6]
     [ 3  6 59]]
    iter:    60
    diff:    0.0006354332508227524
    matrix: 
     [[ 1  2  3]
     [ 2  4  6]
     [ 3  6 39]]
    iter:    80
    diff:    0.002637655251130759
    matrix: 
     [[ 1  2  3]
     [ 2  4  6]
     [ 3  6 19]]
    iter:    100
    diff:    0.0
    matrix: 
     [[1 2 3]
     [2 4 6]
     [3 6 9]]
    iter:    120
    diff:    0.0
    matrix: 
     [[1 2 3]
     [2 4 6]
     [3 6 9]]
    iter:    140
    diff:    0.0
    matrix: 
     [[1 2 3]
     [2 4 6]
     [3 6 9]]
    iter:    160
    diff:    0.0
    matrix: 
     [[1 2 3]
     [2 4 6]
     [3 6 9]]
    iter:    180
    diff:    0.0
    matrix: 
     [[1 2 3]
     [2 4 6]
     [3 6 9]]

``` python
matrix = np.array(
    [[1, 2, 3],
     [2, 4, 6],
     [3, 6, 100]]
)
projection = matrix.copy()
mask = np.array(
    [[False, False, False],
     [False, False, False],
     [False, False, True],]
)
for i in range(200):
    matrix, projection, diff = iteration(matrix, projection, mask, rank=2)
    if i % 20 == 0:
        print("iter:\t", i)
        print("diff:\t", diff)
        print("matrix:\t\n", matrix)
```

    iter:    0
    diff:    8.077935669463166e-32
    matrix: 
     [[ 1  2  3]
     [ 2  4  6]
     [ 3  6 99]]
    iter:    20
    diff:    0.0
    matrix: 
     [[ 1  2  3]
     [ 2  4  6]
     [ 3  6 99]]
    iter:    40
    diff:    0.0
    matrix: 
     [[ 1  2  3]
     [ 2  4  6]
     [ 3  6 99]]
    iter:    60
    diff:    0.0
    matrix: 
     [[ 1  2  3]
     [ 2  4  6]
     [ 3  6 99]]
    iter:    80
    diff:    0.0
    matrix: 
     [[ 1  2  3]
     [ 2  4  6]
     [ 3  6 99]]
    iter:    100
    diff:    0.0
    matrix: 
     [[ 1  2  3]
     [ 2  4  6]
     [ 3  6 99]]
    iter:    120
    diff:    0.0
    matrix: 
     [[ 1  2  3]
     [ 2  4  6]
     [ 3  6 99]]
    iter:    140
    diff:    0.0
    matrix: 
     [[ 1  2  3]
     [ 2  4  6]
     [ 3  6 99]]
    iter:    160
    diff:    0.0
    matrix: 
     [[ 1  2  3]
     [ 2  4  6]
     [ 3  6 99]]
    iter:    180
    diff:    0.0
    matrix: 
     [[ 1  2  3]
     [ 2  4  6]
     [ 3  6 99]]

``` python
matrix = np.array(
    [[1, 2, 3],
     [2, 8, 6],
     [3, 6, 100]]
)
projection = matrix.copy()
mask = np.array(
    [[False, False, False],
     [False, False, False],
     [False, False, True],]
)
for i in range(200):
    matrix, projection, diff = iteration(matrix, projection, mask, rank=2)
    if i % 20 == 0:
        print("iter:\t", i)
        print("diff:\t", diff)
        print("matrix:\t\n", matrix)
```

    iter:    0
    diff:    8.745301605160928e-13
    matrix: 
     [[ 1  2  3]
     [ 2  8  6]
     [ 3  6 99]]
    iter:    20
    diff:    0.00015625177523117403
    matrix: 
     [[ 1  2  3]
     [ 2  8  6]
     [ 3  6 79]]
    iter:    40
    diff:    0.00027778552683950487
    matrix: 
     [[ 1  2  3]
     [ 2  8  6]
     [ 3  6 59]]
    iter:    60
    diff:    0.000625062826647637
    matrix: 
     [[ 1  2  3]
     [ 2  8  6]
     [ 3  6 39]]
    iter:    80
    diff:    0.002502267255650722
    matrix: 
     [[ 1  2  3]
     [ 2  8  6]
     [ 3  6 19]]
    iter:    100
    diff:    0.0
    matrix: 
     [[1 2 3]
     [2 8 6]
     [3 6 9]]
    iter:    120
    diff:    0.0
    matrix: 
     [[1 2 3]
     [2 8 6]
     [3 6 9]]
    iter:    140
    diff:    0.0
    matrix: 
     [[1 2 3]
     [2 8 6]
     [3 6 9]]
    iter:    160
    diff:    0.0
    matrix: 
     [[1 2 3]
     [2 8 6]
     [3 6 9]]
    iter:    180
    diff:    0.0
    matrix: 
     [[1 2 3]
     [2 8 6]
     [3 6 9]]

# Problem 15: Lattice Paths
import copy
n = 2
matrix_line = list(n * ".")

matrix = []
for line in range(2):
    matrix.append(matrix_line)

for line in matrix:
    print(line)
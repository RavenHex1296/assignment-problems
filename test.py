def main_diagonol_and_below(n):
    return [[1 if i == j or i == j + 1 else 0 for j in range(n)] for i in range(n)]

print(main_diagonol_and_below(4))
from __future__ import annotations

from typing import List, Tuple

Matrix = List[List[float]]


# FI: Tämä funktio tarkistaa matriisin koon.
# RU: Эта функция проверяет размерности матриц.
def validate_matrix_dimensions(a: Matrix, b: Matrix, operation: str) -> Tuple[bool, str]:
    if operation in {"add", "subtract"}:
        if len(a) != len(b) or any(len(row_a) != len(row_b) for row_a, row_b in zip(a, b)):
            return False, "Для сложения и вычитания матрицы должны быть одинакового размера."
    elif operation == "multiply":
        if not a or not b or len(a[0]) != len(b):
            return False, "Для умножения число столбцов A должно равняться числу строк B."
    return True, ""


# FI: Tämä funktio laskee kahden matriisin summan.
# RU: Эта функция вычисляет сумму двух матриц.
def add_matrices(a: Matrix, b: Matrix) -> Matrix:
    ok, msg = validate_matrix_dimensions(a, b, "add")
    if not ok:
        raise ValueError(msg)
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


# FI: Tämä funktio laskee kahden matriisin erotuksen.
# RU: Эта функция вычисляет разность двух матриц.
def subtract_matrices(a: Matrix, b: Matrix) -> Matrix:
    ok, msg = validate_matrix_dimensions(a, b, "subtract")
    if not ok:
        raise ValueError(msg)
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


# FI: Tämä funktio kertoo kaksi matriisia.
# RU: Эта функция перемножает две матрицы.
def multiply_matrices(a: Matrix, b: Matrix) -> Matrix:
    ok, msg = validate_matrix_dimensions(a, b, "multiply")
    if not ok:
        raise ValueError(msg)
    rows, cols, inner = len(a), len(b[0]), len(b)
    result: Matrix = [[0.0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = sum(a[i][k] * b[k][j] for k in range(inner))
    return result


# FI: Tämä funktio kertoo matriisin skalaarilla.
# RU: Эта функция умножает матрицу на число.
def multiply_matrix_by_scalar(a: Matrix, scalar: float) -> Matrix:
    return [[value * scalar for value in row] for row in a]


# FI: Tämä funktio transponoi matriisin.
# RU: Эта функция транспонирует матрицу.
def transpose_matrix(a: Matrix) -> Matrix:
    if not a:
        return []
    return [list(row) for row in zip(*a)]


# FI: Tämä funktio laskee determinantin.
# RU: Эта функция вычисляет определитель матрицы.
def determinant(a: Matrix) -> float:
    n = len(a)
    if n == 0 or any(len(row) != n for row in a):
        raise ValueError("Определитель можно вычислить только для квадратной матрицы.")
    if n == 1:
        return a[0][0]
    if n == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]

    det = 0.0
    for col in range(n):
        minor = [row[:col] + row[col + 1 :] for row in a[1:]]
        det += ((-1) ** col) * a[0][col] * determinant(minor)
    return det


# FI: Tämä funktio laskee käänteismatriisin.
# RU: Эта функция вычисляет обратную матрицу.
def inverse_matrix(a: Matrix) -> Matrix:
    n = len(a)
    if n == 0 or any(len(row) != n for row in a):
        raise ValueError("Обратная матрица существует только для квадратной матрицы.")

    det = determinant(a)
    if det == 0:
        raise ValueError("Обратная матрица не существует: определитель равен 0.")

    cofactors: Matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            minor = [r[:j] + r[j + 1 :] for idx, r in enumerate(a) if idx != i]
            row.append(((-1) ** (i + j)) * determinant(minor))
        cofactors.append(row)

    adjugate = transpose_matrix(cofactors)
    return [[adjugate[i][j] / det for j in range(n)] for i in range(n)]


# FI: Tämä funktio luo yksikkömatriisin.
# RU: Эта функция создаёт единичную матрицу.
def create_identity_matrix(size: int) -> Matrix:
    if size <= 0:
        raise ValueError("Размер единичной матрицы должен быть больше 0.")
    return [[1.0 if i == j else 0.0 for j in range(size)] for i in range(size)]

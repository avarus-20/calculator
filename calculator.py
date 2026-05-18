from matrix_utils import (
    add_matrices,
    create_identity_matrix,
    determinant,
    inverse_matrix,
    multiply_matrices,
    multiply_matrix_by_scalar,
    subtract_matrices,
    transpose_matrix,
)


def read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error! Invalid number")


def read_float(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        if raw == "":
            return 0.0
        try:
            return float(raw)
        except ValueError:
            print("Ошибка: введите число (пустое значение считается 0).")


def input_matrix(name: str):
    print(f"\n{name}: ввод матрицы")
    rows = read_int("Количество строк: ")
    cols = read_int("Количество столбцов: ")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(read_float(f"{name}[{i + 1},{j + 1}] = "))
        matrix.append(row)
    return matrix


def print_matrix(title: str, matrix):
    print(f"\n{title}")
    for row in matrix:
        print(" ".join(f"{value:.4g}" for value in row))


def matrix_calculator() -> None:
    matrix_a = input_matrix("Matrix A")
    matrix_b = input_matrix("Matrix B")

    while True:
        print(
            "\nMatrix operations: add, sub, mul, scalar_a, scalar_b, transpose_a, transpose_b, "
            "det_a, det_b, inv_a, inv_b, id, clear, back"
        )
        cmd = input("Choose matrix operation: ").strip().lower()

        try:
            if cmd == "add":
                print_matrix("A + B", add_matrices(matrix_a, matrix_b))
            elif cmd == "sub":
                print_matrix("A - B", subtract_matrices(matrix_a, matrix_b))
            elif cmd == "mul":
                print_matrix("A × B", multiply_matrices(matrix_a, matrix_b))
            elif cmd == "scalar_a":
                scalar = read_float("Scalar for A: ")
                print_matrix("scalar × A", multiply_matrix_by_scalar(matrix_a, scalar))
            elif cmd == "scalar_b":
                scalar = read_float("Scalar for B: ")
                print_matrix("scalar × B", multiply_matrix_by_scalar(matrix_b, scalar))
            elif cmd == "transpose_a":
                print_matrix("Transpose(A)", transpose_matrix(matrix_a))
            elif cmd == "transpose_b":
                print_matrix("Transpose(B)", transpose_matrix(matrix_b))
            elif cmd == "det_a":
                print(f"det(A) = {determinant(matrix_a):.4g}")
            elif cmd == "det_b":
                print(f"det(B) = {determinant(matrix_b):.4g}")
            elif cmd == "inv_a":
                print_matrix("A^-1", inverse_matrix(matrix_a))
            elif cmd == "inv_b":
                print_matrix("B^-1", inverse_matrix(matrix_b))
            elif cmd == "id":
                size = read_int("Identity matrix size: ")
                print_matrix("I", create_identity_matrix(size))
            elif cmd == "clear":
                matrix_a = input_matrix("Matrix A")
                matrix_b = input_matrix("Matrix B")
            elif cmd == "back":
                return
            else:
                print("Ошибка: неизвестная операция.")
        except ValueError as exc:
            print(f"Ошибка: {exc}")


while True:  # бесконечный цикл
    try:
        operation = input("Choose an operation (+,-,*,/,**,%,matrix,exit):").lower()

        if operation == "exit":
            print("Program closed.")
            break

        if operation == "matrix":
            matrix_calculator()
            continue

        num_1 = int(input("Enter the first number : "))
        num_2 = int(input("Enter the second number : "))

        if operation == "+":
            print(num_1 + num_2)

        elif operation == "-":
            print(num_1 - num_2)

        elif operation == "*":
            print(num_1 * num_2)

        elif operation == "/":
            if num_2 != 0:  # / 0
                print(num_1 / num_2)
            else:
                print("Division by 0 is not allowed")

        elif operation == "**":
            print(num_1**num_2)
        elif operation == "%":
            print(num_1 % num_2)

        else:
            print("Error! Enter a valid operation (+,-,*,/,**,%,matrix,exit):")

    except ValueError:  # Ловим ошибку
        print("Error! Invalid number")

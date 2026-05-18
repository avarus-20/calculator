import unittest

from matrix_utils import (
    add_matrices,
    determinant,
    inverse_matrix,
    multiply_matrices,
    subtract_matrices,
    transpose_matrix,
)


class TestMatrixUtils(unittest.TestCase):
    def test_add_matrices(self):
        self.assertEqual(add_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]]), [[6, 8], [10, 12]])

    def test_subtract_matrices(self):
        self.assertEqual(subtract_matrices([[5, 6], [7, 8]], [[1, 2], [3, 4]]), [[4, 4], [4, 4]])

    def test_multiply_matrices(self):
        self.assertEqual(multiply_matrices([[1, 2], [3, 4]], [[2, 0], [1, 2]]), [[4, 4], [10, 8]])

    def test_transpose_matrix(self):
        self.assertEqual(transpose_matrix([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]])

    def test_determinant_2x2(self):
        self.assertEqual(determinant([[4, 6], [3, 8]]), 14)

    def test_determinant_3x3(self):
        self.assertEqual(determinant([[6, 1, 1], [4, -2, 5], [2, 8, 7]]), -306)

    def test_inverse_matrix(self):
        actual = inverse_matrix([[4, 7], [2, 6]])
        expected = [[0.6, -0.7], [-0.2, 0.4]]
        for i in range(2):
            for j in range(2):
                self.assertAlmostEqual(actual[i][j], expected[i][j], places=8)

    def test_invalid_dimensions(self):
        with self.assertRaises(ValueError):
            add_matrices([[1, 2]], [[1], [2]])

    def test_empty_or_invalid_data(self):
        with self.assertRaises(ValueError):
            determinant([])


if __name__ == "__main__":
    unittest.main()

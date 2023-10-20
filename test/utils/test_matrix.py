import sys
#sys.path.append("../../src/")
from unittest import TestCase
from src.utils.matrix import Matrix, LOWER_LEFT, UPPER_LEFT


class TestMatrix(TestCase):
    def test_get_pix_num(self):
        """
        The origin is where the 0th pixel is.  The 0, 0 point should always be the upper left point
        when looking directly at the front (lights) of the matrix.
        """
        # simple 20x20 matrix with 0 pixel upper left and going horizontally
        matrix_ulh = Matrix(20, 20, None, offset=0, origin=UPPER_LEFT, vertical=False)
        assert matrix_ulh
        # origin should be the first pixel since the origin and the upper left coincide
        self.assertEqual(0, matrix_ulh.get_pix_num(0, 0))
        # end of the first row should be just a linear count of the x position
        self.assertEqual(19, matrix_ulh.get_pix_num(19, 0))
        # end of first column should be the last pixel since we are horizontally aligned with even rows
        self.assertEqual(399, matrix_ulh.get_pix_num(0, 19))
        # end of last column and row should be 19 less than the position above
        self.assertEqual(380, matrix_ulh.get_pix_num(19, 19))
        # verify the second row.  end should be one from the end of the first, and start, 19 later
        self.assertEqual(20, matrix_ulh.get_pix_num(19, 1))
        self.assertEqual(39, matrix_ulh.get_pix_num(0, 1))

    def test_compute_pixel_for_upper_left(self):
        """
        simple 20x20 matrix with 0 pixel upper left and going horizontally
        """
        matrix_ulh = Matrix(20, 20, None, offset=0, origin=UPPER_LEFT, vertical=False)
        assert matrix_ulh
        # origin should be the first pixel since the origin and the upper left coincide
        self.assertEqual(0, matrix_ulh.compute_pixel(0, 0))
        # end of the first row should be just a linear count of the x position
        self.assertEqual(19, matrix_ulh.compute_pixel(19, 0))
        # end of first column should be the last pixel since we are horizontally aligned with even rows
        self.assertEqual(399, matrix_ulh.compute_pixel(0, 19))
        # end of last column and row should be 19 less than the position above
        self.assertEqual(380, matrix_ulh.compute_pixel(19, 19))
        # verify the second row.  end should be one from the end of the first, and start, 19 later
        self.assertEqual(20, matrix_ulh.compute_pixel(19, 1))
        self.assertEqual(39, matrix_ulh.compute_pixel(0, 1))

    def test_compute_pixel_for_upper_left_with_offset(self):
        """
        simple 20x20 matrix with 0 pixel upper left and going horizontally, with 1 offset
        """
        matrix_ulh = Matrix(20, 20, None, offset=1, origin=UPPER_LEFT, vertical=False)
        assert matrix_ulh
        # origin should be the first pixel since the origin and the upper left coincide
        self.assertEqual(1, matrix_ulh.compute_pixel(0, 0))
        # end of the first row should be just a linear count of the x position
        self.assertEqual(20, matrix_ulh.compute_pixel(19, 0))
        # end of first column should be the last pixel since we are horizontally aligned with even rows
        self.assertEqual(400, matrix_ulh.compute_pixel(0, 19))
        # end of last column and row should be 19 less than the position above
        self.assertEqual(381, matrix_ulh.compute_pixel(19, 19))
        # verify the second row.  end should be one from the end of the first, and start, 19 later
        self.assertEqual(21, matrix_ulh.compute_pixel(19, 1))
        self.assertEqual(40, matrix_ulh.compute_pixel(0, 1))

    def test_compute_pixel_for_upper_left(self):
        """
        simple 20x20 matrix with 0 pixel lower left and going vertically
        """
        matrix_llv = Matrix(20, 20, None, offset=0, origin=LOWER_LEFT, vertical=True)
        assert matrix_llv
        # origin should be the 19th pixel since counting from bottom up to origin
        self.assertEqual(19, matrix_llv.compute_pixel(0, 0))
        # end of the first row should be 19 less than the last pixel
        self.assertEqual(380, matrix_llv.compute_pixel(19, 0))
        # end of first column should be the origin since we are LL
        self.assertEqual(0, matrix_llv.compute_pixel(0, 19))
        # end of last column and row should be last pixel
        self.assertEqual(399, matrix_llv.compute_pixel(19, 19))
        # verify the second row.  end should be 18 before last.  start should be at 18
        self.assertEqual(381, matrix_llv.compute_pixel(19, 1))
        self.assertEqual(18, matrix_llv.compute_pixel(0, 1))

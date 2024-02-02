import unittest
from app import calculate_cube_volume, calculate_sphere_volume

class TestAppMethods(unittest.TestCase):

    def test_calculate_cube_volume(self):
        # Test with valid input
        result = calculate_cube_volume(2.0, 2)
        self.assertEqual(result, '8.00')

        # Test with zero length
        result = calculate_cube_volume(0, 2)
        self.assertEqual(result, '0.00')

        # Test with negative length (assuming your application should handle this case)
        result = calculate_cube_volume(-3.5, 2)
        self.assertEqual(result, '-42.88')  # Update with the expected result

    def test_calculate_sphere_volume(self):
        # Test with valid input
        result = calculate_sphere_volume(1.0, 2)
        self.assertEqual(result, '4.19')

        # Test with zero radius
        result = calculate_sphere_volume(0, 2)
        self.assertEqual(result, '0.00')

        # Test with negative radius (assuming your application should handle this case)
        result = calculate_sphere_volume(-2.5, 2)
        self.assertEqual(result, '-65.45')  # Update with the expected result

if __name__ == '__main__':
    unittest.main()

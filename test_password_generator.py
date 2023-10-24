import unittest
import password_generator

class TestPasswordGenerator(unittest.TestCase):
    def test_password_generation_properties(self):
        password_length = 10
        password = password_generator.random_list(password_length)
        
        self.assertIsInstance(password, str)  # Check if the result is a string
        self.assertEqual(len(password), password_length)  # Check if the length matches the requested length

if __name__ == '__main__':
    unittest.main()

import unittest
import password_generator

class TestPasswordGenerator(unittest.TestCase):
    def test_password_generation(self):
        password_length = 10
        password = password_generator.random_list(password_length)
        
        self.assertIsInstance(password, str)  # Check if the result is a string
        self.assertEqual(len(password), password_length)  # Check if the length matches the requested length

    def test_password_with_uppercase(self):
        password_length = 10
        password_generator.a = 1  # Set the condition to include at least one capital letter
        password = password_generator.random_list(password_length)

        self.assertIsInstance(password, str)  # Check if the result is a string
        self.assertEqual(len(password), password_length)  # Check if the length matches the requested length
        self.assertTrue(any(char.isupper() for char in password), "The password should contain at least one capital letter")

if __name__ == '__main__':
    unittest.main()

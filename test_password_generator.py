import string
import unittest

from password_generator import generate_password


class TestPasswordGenerator(unittest.TestCase):
    def test_default_password_has_16_characters(self):
        password = generate_password()
        self.assertEqual(len(password), 16)

    def test_custom_password_length(self):
        password = generate_password(24)
        self.assertEqual(len(password), 24)

    def test_password_uses_allowed_characters(self):
        password = generate_password(16)
        allowed_characters = (
            string.ascii_letters + string.digits + string.punctuation
        )
        self.assertTrue(
            all(character in allowed_characters for character in password)
        )

    def test_short_password_raises_value_error(self):
        with self.assertRaises(ValueError):
            generate_password(7)

    def test_non_integer_length_raises_type_error(self):
        with self.assertRaises(TypeError):
            generate_password("16")


if __name__ == "__main__":
    unittest.main()

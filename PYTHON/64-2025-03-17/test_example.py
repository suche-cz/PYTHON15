import unittest
from func import is_username_valid


class TestUsernameIsValid(unittest.TestCase):
    def test_low_length(self):
        self.assertEqual(is_username_valid('x'), False)
    
    def test_ok_length(self):
        self.assertEqual(is_username_valid('suche'), True)
    
    def test_large_length(self):
        self.assertEqual(is_username_valid('qwertzuiopasdfghjklXCVBN'), False)
    
    def test_valid_chars(self):
        username = 'some-ok-username'
        result = is_username_valid(username)
        self.assertEqual(result, True)

    def test_invalid_chars(self):
        username = 'some!ok-username'
        result = is_username_valid(username)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()

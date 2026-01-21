import unittest
from user_validation import valid_email, valid_password
#performming unittest for user validation
class TestUserValidation(unittest.TestCase):
    #testing valid user email
    def test_valid_email(self):
        self.assertTrue(valid_email("abc@gmail.com"))
    #testing invalid user email
    def test_invalid_email(self):
        self.assertFalse(valid_email("abc@.com"))
    #testing valid user password
    def test_valid_password(self):
        self.assertTrue(valid_password("Abc@1234"))
    #testing invalid user password
    def test_invalid_password(self):
        self.assertFalse(valid_password("abc123"))

if __name__ == "__main__":
    unittest.main()

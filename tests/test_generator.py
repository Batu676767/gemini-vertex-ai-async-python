import unittest
from src.utils.is_image_url import is_image_url

class TestUtils(unittest.TestCase):
    def test_is_image_url_valid(self):
        self.assertTrue(is_image_url("http://example.com/image.jpg"))
        self.assertTrue(is_image_url("http://example.com/image.PNG"))

    def test_is_image_url_invalid(self):
        self.assertFalse(is_image_url("http://example.com/file.txt"))
        self.assertFalse(is_image_url("http://example.com/image"))

if __name__ == '__main__':
    unittest.main()

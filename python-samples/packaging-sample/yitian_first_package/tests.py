import unittest
from yitian_first_package.simple import hello_world, fetch_msg


class MyUnitTest(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), 'Hello Python!')

    def test_fetch_msg(self):
        self.assertEqual(fetch_msg(), '你好，Python！')


if __name__ == '__main__':
    unittest.main()

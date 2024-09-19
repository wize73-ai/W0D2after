# ```python
# test_main.py
import unittest
from main import hello_world, greet_person

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello from James!")

    def test_greet_person(self):
        self.assertEqual(greet_person("James"), "Hello, James")

if __name__ == '__main__':
    unittest.main()
# ```
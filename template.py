import unittest

class MyClass():

    def main(self):
        pass

class Tests(unittest.TestCase):

    def setUp(self):
        self.object = MyClass() 

    def test_shouldFail(self):
        self.fail("Initial Fail for Setup")


if __name__ == '__main__':
    unittest.main()

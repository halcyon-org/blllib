import unittest
import blllib

## just print the version of the library
print(blllib.__version__)

class test_Server(unittest.TestCase):
    def test_server(self):
        self.assertEqual(blllib.server(), "server")

if __name__ == '__main__':
    unittest.main()
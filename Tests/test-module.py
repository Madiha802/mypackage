import unittest
from mon_package.module import hello_world
from io import StringIO
import sys

class TestModule(unittest.TestCase):
    def test_hello_world_output(self):
        """
        Teste si la fonction hello_world() affiche correctement 'Hello, world!'.
        """
    
        captured_output = StringIO()
        sys.stdout = captured_output


        hello_world()

        sys.stdout = sys.__stdout__


        self.assertEqual(captured_output.getvalue().strip(), "Hello, world!")

if __name__ == '__main__':
    unittest.main()

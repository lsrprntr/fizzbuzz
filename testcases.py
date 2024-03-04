import fizzbuzz
import unittest
import sys
import io

class TestFizzBuzz(unittest.TestCase):
    def test_edgeCases(self):
        fizzbuzz.fizzbuzz(1,3)
        capture = sys.stdout
        out = io.StringIO()
        sys.stdout = out
        output = out.getvalue().strip()
        expected = '''
        1
        2
        3 fizz
        '''
        assert output == expected      
        #self.assertEqual(fizzbuzz.fizzbuzz(1,3), 0)
        #self.assertEqual(fizzbuzz.fizzbuzz(99,100), 0)


    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    try:
        unittest.main()
    except:
        pass
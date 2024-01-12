import unittest
from To_do_list import*

class MyTest(unittest.TestCase):
    def test_add_task(self):
        result = add_task()
        self.assertTrue(result)


if __name__=="__main__":
    unittest.main
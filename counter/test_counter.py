"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""

import unittest
from counter import Counter


class TestCounter(unittest.TestCase):

    def setUp(self):
        self.counter = Counter()
        self.counter2 = Counter

    def test_New_references(self):
        self.counter2 = Counter()
        self.assertEqual(self.counter.count, self.counter2.count)

    def test_new_references_with_increment(self):
        self.counter2 = Counter()
        self.counter.increment()
        self.assertEqual(self.counter.count, self.counter2.count)
        self.counter2.increment()
        self.assertEqual(self.counter.count, self.counter2.count)


if __name__ == '__main__':
    unittest.main()

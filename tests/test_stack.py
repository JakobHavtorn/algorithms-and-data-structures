import unittest
from context import data_structures
from data_structures import Stack


class StackTest(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(AssertionError):
            Stack(max_size=-1)
        self.assertEqual(Stack(max_size=0)._max_size, 0)
        self.assertEqual(Stack(max_size=1)._max_size, 1)
        self.assertEqual(Stack(max_size=10)._max_size, 10)

    def test_push(self):
        s = Stack(max_size=2)
        s.push(1)
        s.push(2)
        with self.assertRaises(IndexError):
            s.push(3)

    def test_pop(self):
        with self.assertRaises(IndexError):
            s = Stack(max_size=2)
            s.pop()
        s = Stack(max_size=2)
        s.push(42)
        self.assertEqual(s.pop(), 42)

    def test_peek(self):
        s = Stack(max_size=2)
        self.assertEqual(s.peek(), None)
        s.push(42)
        self.assertEqual(s.peek(), 42)
        s.push(43)
        self.assertEqual(s.peek(), 43)

    def test_is_empty(self):
        s = Stack(max_size=2)
        self.assertEqual(s.is_empty(), True)
        s.push(42)
        self.assertEqual(s.is_empty(), False)
        s.pop()
        self.assertEqual(s.is_empty(), True)

    def test_is_full(self):
        s = Stack(max_size=2)
        self.assertEqual(s.is_full(), False)
        s.push(42)
        self.assertEqual(s.is_full(), False)
        s.push(43)
        self.assertEqual(s.is_full(), True)
        s.pop()
        self.assertEqual(s.is_full(), False)

if __name__ == '__main__':
    unittest.main()
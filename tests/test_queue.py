import unittest
from context import data_structures
from data_structures import Queue


class QueueTest(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(AssertionError):
            Queue(max_size=-1)
        self.assertEqual(Queue(max_size=0)._max_size, 0)
        self.assertEqual(Queue(max_size=1)._max_size, 1)
        self.assertEqual(Queue(max_size=10)._max_size, 10)

    def test_enqueue(self):
        q = Queue(max_size=2)
        q.enqueue(1)
        q.enqueue(2)
        with self.assertRaises(IndexError):
            q.enqueue(3)

    def test_dequeue(self):
        with self.assertRaises(IndexError):
            q = Queue(max_size=2)
            q.dequeue()
        q = Queue(max_size=2)
        q.enqueue(42)
        q.enqueue(43)
        self.assertEqual(q.dequeue(), 42)
        self.assertEqual(q.dequeue(), 43)
        with self.assertRaises(IndexError):
            q = Queue(max_size=2)
            q.dequeue()

    def test_enqueue_dequeue_circular(self):
        q = Queue(max_size=3)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        for i in range(4, 10):
            self.assertEqual(q.dequeue(), i - 3)
            q.enqueue(i)

    def test_peek(self):
        q = Queue(max_size=2)
        self.assertEqual(q.peek(), None)
        q.enqueue(42)
        self.assertEqual(q.peek(), 42)
        q.enqueue(43)
        self.assertEqual(q.peek(), 42)

    def test_is_empty(self):
        q = Queue(max_size=2)
        self.assertEqual(q.is_empty(), True)
        q.enqueue(42)
        self.assertEqual(q.is_empty(), False)
        q.dequeue()
        self.assertEqual(q.is_empty(), True)

    def test_is_full(self):
        q = Queue(max_size=2)
        self.assertEqual(q.is_full(), False)
        q.enqueue(42)
        self.assertEqual(q.is_full(), False)
        q.enqueue(43)
        self.assertEqual(q.is_full(), True)
        q.dequeue()
        self.assertEqual(q.is_full(), False)

if __name__ == '__main__':
    unittest.main()
    
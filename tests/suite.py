from test_stack import StackTest
from test_queue import QueueTest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(StackTest)
    suite.addTest(QueueTest)
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

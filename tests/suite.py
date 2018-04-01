from test_stack import StackTest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(StackTest)
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
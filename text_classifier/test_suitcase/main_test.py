import sys
sys.path.insert(0, '/home/jan/Development/Text_Classifier')

from test_suit import TestSuits
# Author Jan Wessling


"""
Main-Module for testing the Text-Classifier-System

Set up your testing environment here.
-------------------------------------

"""

if __name__ == '__main__':
    system_test = TestSuits(test_name="system_test")
    attribute_test = TestSuits(test_name="attribute_test")
    variety_test = TestSuits(test_name="variety_test")
    # system_test.run_test()
    # attribute_test.run_test()
    variety_test.run_test()

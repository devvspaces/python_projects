"""
Test suite for format function in "Stopwatch - The game"
"""

from suite import MyTestSuite

def run_suite(format_function):
    """
    Some informal testing code
    """
    
    # create a TestSuite object
    suite = MyTestSuite()
    
    # test format_function on various inputs
    suite.run_test(format_function(0), "0:00.0")
    suite.run_test(format_function(7), "0:00.7")
    suite.run_test(format_function(17), "0:01.7")
    suite.run_test(format_function(60), "0:06.0")
    suite.run_test(format_function(63), "0:06.3")
    suite.run_test(format_function(214), "0:21.4")
    suite.run_test(format_function(599), "0:59.9")
    suite.run_test(format_function(600), "1:00.0")
    suite.run_test(format_function(602), "1:00.2")
    suite.run_test(format_function(667), "1:06.7")
    suite.run_test(format_function(1325), "2:12.5")
    suite.run_test(format_function(4567), "7:36.7")
    suite.run_test(format_function(5999), "9:59.9")
    
    suite.fetch_results()
    
    




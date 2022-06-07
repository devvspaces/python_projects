"""
Format function for a stopwatch
"""

from tests import run_suite
    
def stopwatch_format(ticks):
    """
    Convert tenths of seconds to formatted time
    """
    
    minutes = ticks // 600
    # minutes = ticks // 60
    tens_seconds =  (ticks // 100) % 6
    seconds = (ticks // 10) % 10
    tenths = ticks % 10
    return str(minutes) + ':' + str(tens_seconds) + \
           str(seconds) + '.' + str(tenths)
    
# run the testing suite for our format function
run_suite(stopwatch_format)
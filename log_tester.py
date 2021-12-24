#from LogManager import Logger
import LogManager
        
# Test Code 
logger = LogManager.Logger();
logger.set_log_level(logger.INFO)
#logger.set_log_suffix('sdc')
            
# Usage:
# $ python3 log_tester.py;ll -t default.log*
        
if __name__ == '__main__':
    for _ in range(5000):
        logger.error('message')
        logger.info('message')
        logger.warn('message')
        logger.debug('message')

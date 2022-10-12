# logger4py
logger4py is just another python Logger Implementation. Ispired by the [Log4Shell](https://en.wikipedia.org/wiki/Log4Shell) fiasco.

Example 1:
```
import LogManager
logger = LogManager.Logger();
logger.set_log_level(logger.INFO)
logger.error('message')
logger.info('message')
logger.warn('message')
logger.debug('message')
```

Example 2: Testing exceptions and other use cases.
```
import LogManager
logger = LogManager.Logger();
logger.set_log_level(logger.INFO)
warn_condition = false

try:
  # Log the obvious. Something happened make a record of it in the logs.
  logger.info('message: log something obvious.')
  
 if warn_condition == true:
    logger.warn('message: log a warning when a condition occured.')
except:
  # Something went wrong
  logger.debug('message: something went wrong')

```

Example 3: Test log file threshholds.

```
#from LogManager import Logger
import LogManager

# Test Code
logger = LogManager.Logger();
logger.set_log_level(logger.INFO)
#logger.set_log_suffix('sdc')

# Usage:
# $ python3 file.py;ll -t default.log*

if __name__ == '__main__':
    for _ in range(5000):
        logger.error('message')
        logger.info('message')
        logger.warn('message')
        logger.debug('message')
```

# Usage:
```
$ python3 log_tester.py;ls -lt default.log*
-rw-r--r--  1 tcwbot  staff   697317 Dec 24 02:42 default.log
-rw-r--r--  1 tcwbot  staff  1000006 Dec 24 02:42 default.log.1
-rw-r--r--  1 tcwbot  staff  1000006 Dec 24 02:42 default.log.2
-rw-r--r--  1 tcwbot  staff  1000006 Dec 24 02:21 default.log.3
-rw-r--r--  1 tcwbot  staff  1000006 Dec 24 02:21 default.log.4
-rw-r--r--  1 tcwbot  staff  1000006 Dec 24 02:21 default.log.5
-rw-r--r--  1 tcwbot  staff  1000006 Dec 24 02:21 default.log.6
-rw-r--r--  1 tcwbot  staff  1000006 Dec 24 02:21 default.log.7
-rw-r--r--  1 tcwbot  staff  1000006 Dec 24 02:21 default.log.8
-rw-r--r--  1 tcwbot  staff  1000006 Dec 24 02:21 default.log.9
-rw-r--r--  1 tcwbot  staff  1000006 Dec 24 02:21 default.log.10
```

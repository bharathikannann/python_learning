# Basic implementations of logging in Python
import logging

# Basic logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Format the log message
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

# Handler to write to a file
handler = logging.FileHandler('test.log')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

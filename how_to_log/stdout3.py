import sys
import logging

# Define a custom stream handler that redirects stdout to a file-like object
class StdoutHandler(logging.StreamHandler):
    def __init__(self, stream=None):
        super().__init__(stream)
        self.buffer = ''

    def emit(self, record):
        msg = self.format(record)
        self.buffer += msg + '\n'
        if record.levelno >= logging.WARNING:
            self.flush()

    def flush(self):
        self.stream.write(self.buffer)
        self.buffer = ''

# Create a logger object
logger = logging.getLogger('mylogger')
logger.setLevel(logging.INFO)

# Create a file handler
file_handler = logging.FileHandler('mylog.txt')
file_handler.setLevel(logging.INFO)

# Create a custom stream handler to capture stdout
stdout_handler = StdoutHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stdout_handler)

# Test the logger
logger.info('This message will be logged to both the file and the console')
import os
os.system("dir")

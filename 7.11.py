from queue import Queue 
from functools import wraps

class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args


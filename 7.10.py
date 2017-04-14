def apply_async(func, args, *, callback):
    #compute the result
    result = func(*args)
    #invoke the callback
    callback(result)

class ResultHandle:
    def __init__(self):
        self.sequence = 0
    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))

def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

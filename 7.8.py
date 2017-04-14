def out_result(result, log = None):
    if log is not None:
        log.debug('Got: %r', result)

def add(x, y):
    return x + y

if __name__ == '__main__':
    import logging
    from multiprocessing import Pool
    from functools import partial

    logging.basicConfig(level = logging.DEBUG)
    log = logging.getLogger('test')
    log2 = logging.getLogger('test2')

    p = Pool()
    p.apply_async(add, (3, 4), callback = partial(out_result, log = log))
    p.apply_async(add, (3, 4), callback = partial(out_result, log = log))
    p.apply_async(add, (5, 6), callback = partial(out_result, log = log2))
    p.close()
    p.join()

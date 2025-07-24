import time
import os
import psutil

def elapsed_since(start):
    return time.strftime('%H:%M:%S', time.gmtime(time.time() - start))

def get_process_memory():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss

def track(func):
    def wrapper(*args, **kwargs):
        mem_before = get_process_memory()
        start = time.time()
        result = func(*args, **kwargs)
        elapsed_time = elapsed_since(start)
        mem_after = get_process_memory()
        print('---------------------')
        print('{}:\n\tmemory before: {:,} Bytes\n\tmemory after: {:,} Bytes\n\tmemory consumed: {:,} Bytes\n\texec time: {}s'.format(
            func.__name__,
            mem_before, mem_after, mem_after - mem_before,
            elapsed_time
        ))
        print('---------------------')
        return result
    return wrapper
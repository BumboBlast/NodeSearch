import time
import os
# import psutil

def elapsed_since(start):
    return time.strftime('%H:%M:%S', time.gmtime(time.time() - start))

# def get_process_memory():
    # process = psutil.Process(os.getpid())
    # return process.memory_info().rss

def track(func):
    def wrapper(*args, **kwargs):
        # mem_before = get_process_memory()
        mem_before = 0
        start = time.time()
        result = func(*args, **kwargs)
        elapsed_time = elapsed_since(start)
        # mem_after = get_process_memory()
        mem_after = 0
        print("---------------------")
        print(
            f"{func.__name__}:\n",
            f"\tmemory before: {mem_before} Bytes\n",
            f"\tmemory after: {mem_after} Bytes\n",
            f"\tmemory consumed: {mem_after - mem_before} Bytes\n",
            f"\texec time: {elapsed_time}s"
        )
        print('---------------------')
        return result
    return wrapper

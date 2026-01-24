
UNITS : dict = {
    0 : "",
    1 : "bytes",
    2 : "bytes",
    3 : "Kb",
    4 : "Kb",
    5 : "Kb",
    6 : "Mb",
    7 : "Mb",
    8 : "Mb",
    9 : "Gb",
}

try:
    import time
    import os
    import math
    import psutil

    def elapsed_since(start):
        return time.strftime('%H:%M:%S', time.gmtime(time.time() - start))

    def get_process_memory():
        process = psutil.Process(os.getpid())
        return process.memory_info().rss

    def track(func):
        def wrapper(*args, **kwargs):
            # get metrics
            mem_before = get_process_memory()
            start = time.time()
            result = func(*args, **kwargs)
            elapsed_time = elapsed_since(start)
            mem_after = get_process_memory()

            # choose approrpiate label
            unit : str = "Bytes"
            roundedMemBefore : float = mem_before
            roundedMemAfter : float = mem_after
            roundedMemComsumed : float = mem_after - mem_before
            order : int = math.floor(math.log(mem_before, 10))
            if order in UNITS:
                unit = UNITS[order]
                roundedMemBefore = round(roundedMemBefore / int(10 ** (order - 1)), 3)
                roundedMemAfter = round(roundedMemAfter / int(10 ** (order - 1)), 3)
                roundedMemComsumed = round(roundedMemComsumed / int(10 ** (order - 1)), 3)
                
            print("---------------------")
            print(
                f"{func.__name__}:\n",
                f"\tmemory before:\t{roundedMemBefore} {unit}\n",
                f"\tmemory after:\t{roundedMemAfter} {unit}\n",
                f"\tmemory consumed:{roundedMemComsumed} {unit}\n",
                f"\texec time: {elapsed_time}s",
            )
            print('---------------------')
            return result
        return wrapper
except:
    import time
    import os

    def elapsed_since(start):
        return time.strftime('%H:%M:%S', time.gmtime(time.time() - start))

    def track(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            elapsed_time = elapsed_since(start)
            print("---------------------")
            print(
                f"{func.__name__}:\n",
                f"\texec time: {elapsed_time}s",
            )
            print('---------------------')
            return result
        return wrapper
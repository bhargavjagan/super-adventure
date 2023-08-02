import time, os, psutil

# inner psutil function
def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info

# decorator function
def profile(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        mem_before = process_memory()
        result = func(*args, **kwargs)
        mem_after = process_memory()
        print("Function Name:",
              func.__name__,
              '\n',
             "Time Taken : ",
             time.time() - start_time,
             '\n',
             "Memory Consumed : ",
             mem_before,
             mem_after,
             mem_after - mem_before,
        )
        return result
    return wrapper
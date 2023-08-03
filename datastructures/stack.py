class Stack:

    def __init__(self) -> None:
        self.arr = []
    
    def push(self) -> None:
        pass

    def pop(self) -> int:
        pass

    def length(self) -> int:
        pass


def logger( func ):
    def wrapper(*args, **kwargs):
        import time
        start_time = time.time()
        result = func(*args, **kwargs)
        print(start_time - time.time())
        return result
    return wrapper


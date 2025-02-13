import time
import random

def decorator_1(func):
    def task_three(*args, **kwargs):
        initial = time.time()
        result = func(*args, **kwargs)
        ending = time.time()
        executionn = ending - initial
        print(f"{func.__name__} call executed in {executionn:.4f} sec")
        return result
    return task_three

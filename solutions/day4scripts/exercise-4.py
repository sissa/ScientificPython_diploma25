# Exercise 4:
# Create a decorator to time a function execution time. Hint: use import time and time_point=time.time(). You can check if it's correct by timing the time.sleep function.

import time 

def time_decorator(func):
    def wrapper(*args, **kwargs):
        time_point = time.time()
        output = func(*args, **kwargs)
        print("Function execution time: ", time.time() - time_point)
        return output
    return wrapper
    

@time_decorator
def sleep():
    time.sleep(3)

@time_decorator
def dot_product(a, b):
    return sum([a[i]*b[i] for i in range(len(a))])

if __name__ == "__main__":

    sleep()

    a = [1, 2, 3]
    b = [4, 5, 6]
    c = dot_product(a, b)

    print('Dot product: ', c)




import functools
def check_empty(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if any(arg == [] for arg in args) or any(value == [] for value in kwargs.values()):
            print("I don't work with empty arrays")
        else:
            return func(*args, **kwargs)
    return wrapper

@check_empty
def print_array(arr):
    '''I print arrays'''
    print(arr)

@check_empty
def print_multiple_arrays(arr1, arr2, arr3=[1]):
    '''I print multiple arrays'''
    print(arr1, arr2, arr3)



if __name__=="__main__":
    l=[1,2,3]
    m=[]
    print("passing an ok array:")
    print_array(l)
    print("passing a non-ok array:")
    print_array(m)
    print("passing 2 ok arrays:")
    print_multiple_arrays(l, l)  
    print("passing non-ok arrays:")
    print_multiple_arrays(l, m)  
    print_multiple_arrays(l, l, arr3=[]) 

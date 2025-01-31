import functools
def check_empty(func):
    @functools.wraps(func)
    def wrapper(arg):
        if arg==[]:
            return print("I don't work with empty arrays")
        else:
            return func(arg)
    return wrapper

@check_empty
def print_array(arr):
    '''I print arrays'''
    print(arr)

if __name__=="__main__":
    l=[1,2,3]
    m=[]
    print_array(l)
    print_array(m)

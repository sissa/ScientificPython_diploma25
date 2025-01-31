import numpy as np
import matplotlib.pyplot as plt

def plot_decorator(func):
    def wrapper(*args, **kwargs):
        # Generate 100 points between 1 and 10
        x = np.linspace(1, 10, 100)
        y = func(x)

        # Plotting
        plt.figure(figsize=(8, 6), facecolor='yellow')
        plt.plot(x, y, color='green')
        plt.title(f"Plot of {func.__name__}")
        plt.xlabel('x')
        plt.ylabel(f'{func.__name__}(x)')
        plt.grid(True)
        plt.show()

        return func(*args, **kwargs)
    return wrapper

# Example usage
@plot_decorator
def my_function(x):
    return np.sin(x)

# Call the decorated function
my_function(1)
 

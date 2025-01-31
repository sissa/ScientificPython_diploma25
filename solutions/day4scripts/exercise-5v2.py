import numpy as np
import matplotlib.pyplot as plt

def plot_decorator(func):
    def wrapper(*args, **kwargs):
        # Generate 100 points between 1 and 10
        x = np.linspace(1, 10, 100)
        y = func(x)

        # Create a figure and axis object
        fig, ax = plt.subplots(figsize=(8, 6))
        fig.patch.set_facecolor('yellow')  # Set the background color of the figure

        # Plotting using the ax interface
        ax.plot(x, y, color='green')
        ax.set_title(f"Plot of {func.__name__}")
        ax.set_xlabel('x')
        ax.set_ylabel(f'{func.__name__}(x)')
        ax.grid(True)

        # Display the plot
        plt.show()

        return func(*args, **kwargs)
    return wrapper

# Example usage
@plot_decorator
def my_function(x):
    return np.sin(x)

# Call the decorated function
my_function(1)
 

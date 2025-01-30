**DO ALL THE EXERCISES OF TODAY IN PURE PYTHON SCRIPTS WITH NO JUPYTER**

#### Exercise 1:

Turn all the exercises of yesterday into `.py` scripts. Save some of the pictures to a file instead of just displaying them (if you are on WSL, chances are you can't display them anyway).

#### Exercise 2:

Turn the solution of the recaman exercise from day one into a module (that has 2 functions). Import it in another script and time the functions from there.

#### Exercise 3:

Create a decorator that checks if the passed array is empty and only calls the function if it's not.

#### Exercise 4:

Create a decorator to time a function execution time. Hint: use `import time` and `time_point=time.time()`. You can check if it's correct by timing the `time.sleep` function.

#### Exercise 5:

Write a decorator that plots a function (of one variable) over the interval (0,100). Make sure your plot has a name, the axis names, nice color, changed background color and a legend.

Do the same using a different "interface".

#### Exercise 6:
Create a class Person that represents a person and has the following attributes:

 - first_name: The first name of the person.
 - last_name: The last name of the person.
 - age: The age of the person.

And the following methods:

 - full_name: Returns the full name of the person, which is the combination of their first and last name.
 - is_adult: Returns True if the person is 18 years or older, and False otherwise.

#### Exercise 7:
Create your own class for complex numbers. Make sure all the arithmetic operations work and that you can print it.

#### Exercise 8:
Create a "wrapper class" for around numpy array for operations on matrices. You should be able to execute the following code:

```
N=4
matrix1=MyMatrix(N) #creates a square matrix
matrix2=MyMatrix(N)
print(matrix1.inverse())
print(matrix1.determinant())
print(matrix1.eigenvalues())
print(matrix1+matrix2)
print(matrix1*matrix2)
```






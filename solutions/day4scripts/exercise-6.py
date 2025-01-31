# Exercise 6
# Create a class Person that represents a person and has the following attributes:
#
# first_name: The first name of the person.
# last_name: The last name of the person.
# age: The age of the person.

# Class Person
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name  = last_name
        self.age        = age
    def full_name(self):
        return self.first_name+" "+self.last_name
    def adult(self):
      return self.age>=18


if __name__ == "__main__":

    # Create a person
    person1 = Person("John", "Doe", 30)
    person2 = Person("Cat", "Meow", 15)
    print(person1.full_name())
    print(person1.adult())
    print(person2.full_name())
    print(person2.adult())
    
   

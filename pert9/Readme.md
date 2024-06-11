# 1. Definition

Arrays (in python) are structures that can store and organize data sets. Data structures talk about a way to store, organize, group and represent data. Data structures are very important and must be mastered by a programmer. On programming forums, I often come across questions that I think can be solved if the person understands the concept of data structures.

In this material, we will discuss advanced data structures, namely sets and dictionaries.

# 2. Set

A set in the python programming language is a collective data type that is used to store multiple values in a single variable with the following conditions:
a.stored member values must be unique (not duplicates)
b.The value of the member that has been entered cannot be changed anymore
c.set is unordered aka unordered-which means it can't be accessed by index.

To better understand the 3 points above, we will immediately do the practice.
General form of Sets:

# use curly braces
student_set = {'Huda', 'Lendis', 'Wahid', 'Basith'} print(student_set)
print(student_set)

# convert list into set
fruit_set = set(['mango', 'Apple']) print(set_fruit)
print(set_fruit)


# sets with different data types
set_mix = {'man', 'animal', 5, True, ('A', 'B')}
print(set_mix)

Outputs:
{'Wahid', 'Lendis', 'Basith', 'Huda'}
{'apel', 'mangga'}
(True, 5, ('A', 'B'), 'hewan', 'manusia'}

# a. Unordered (Set)
The data set type is unordered. That means, we can't use index to access the values error: in the set. Even if we force, we will only get an

my_set = {'a'}
print(my_set[8])

Error message:
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'set' object is note subscriptable

We can also look at the program code that we created earlier:
student_set = {'Huda', 'Lendis', 'Wahid', 'Basith'} print(student_set)

Outputs:
"Wahid", "Lendis", "Basith", "Huda"}
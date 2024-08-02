#Syntax Error
#Syntax errors occur when Python can't understand the code because it doesn't follow the proper syntax rules.

#Example: Missing colon in an if statement
if x > 10
    print("x is greater than 10")

#o/p: Error: SyntaxError: expected ':'.

#Example: Unmatched parentheses
print("Hello World"

#o/p: Error: SyntaxError: unexpected EOF while parsing

#Exceptions
#Exceptions are errors that occur during program execution. Here are some common types

#1 - ZeroDivisionError: Raised when dividing by zero.
x = 10 / 0

#o/p:Error: ZeroDivisionError: division by zero

#2 - IndexError: Raised when trying to access an index that is out of range in a list or tuple.
my_list = [1, 2, 3]
print(my_list[5])

#o/p:Error: IndexError: list index out of range

#3 - KeyError: Raised when a dictionary key is not found.
my_dict = {'a': 1}
print(my_dict['b'])

#o/p: Error: KeyError: 'b'

#4 - TypeError: Raised when an operation or function is applied to an object of inappropriate type.
x = 'hello' + 5

#o/p: Error: TypeError: can only concatenate str (not "int") to str

#5 - ValueError: Raised when a function receives an argument of the right type but inappropriate value.
int('abc')

#o/p: Error: ValueError: invalid literal for int() with base 10: 'abc'

#6 - AttributeError: Raised when an invalid attribute reference is made.
x = 5
x.append(3)

#o/p: Error: AttributeError: 'int' object has no attribute 'append'

#7 - FileNotFoundError: Raised when trying to open a file that does not exist.
with open('nonexistent_file.txt', 'r') as f:
    content = f.read()

#o/p: Error: FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent_file.txt'

#8 - ImportError: Raised when an import statement fails.
import non_existent_module

#o/p: Error: ImportError: No module named 'non_existent_module'

#9 - NameError: Raised when a local or global name is not found.
print(unknown_variable)

#o/p: Error: NameError: name 'unknown_variable' is not defined

#10 - OverflowError: Raised when a calculation exceeds the limits of the data type.
import math
math.exp(1000)

#o/p: Error: OverflowError: math range error

#Handling Exceptions
#You can handle exceptions using try and except blocks:
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")











---
title: My Python Adventure
feed: show
date: 17-10-2023
---
*********
<font size="+3">This is the page that I will share my adventure along the way of learning python.
</font>
<br><br>
The definition of a computer is "an electronic device that **manipulates information, or data** in a dictionary" basically it is a machine that processes data just like all the other machines. Based on this mindset we can relate computers working principle with the functions in mathematics. ***f(x)= 2x+5*** meaning in order to find ***f(x)*** the variable ***x*** should be multiplied by ***2*** and aded ***5*** to that multiplication. Essentially functions are there to "**manipulate information, or data**" for you in a program with a lot of them bonded together. 
<br>
```c
print("Hello World")
```
Is the simplest form of function in **Python** it is used for writing the string (a sequence of characters) to the launcher window.
<br>
<br>
In addition to functions there are some other term as well: **Variables** 
We use variables to temporarily store data in computer’s memory.

```python
price = 31

rating = 6.9

blog_name = ‘Python Adventure’

is_published = True
```
**In the above example,**

• ``price`` is an integer (a whole number without a decimal point)

• ``rating`` is a float (a number with a decimal point)

• ``blog_name`` is a string (a sequence of characters)

• ``is_published`` is a boolean. Boolean values can be True or False.



*********
Simple Weight Converter (kg to lbs):
```python
weight_lbs = int(input('What is your weight in terms of kg: '))  
weight_kg: float = weight_lbs * 2.2  
print('Weight in lb: ')  
print(weight_kg)
```


**Indexes:**
In python indexes start from 0.
this value can be (-) this means index starts from the end of the string
``print(variable[:])`` 


There are two ways to add variables in a string:
**Ane of them is using + command.**
*As shown in* ***message*** *variable*:
**Another one is f string method**
In this method instead of opening and closing the string and adding them one by one, we just open some *holes* in the string with {} 
*As shown in* ***msg*** *variable*:

```python
first_name = 'Yigit'  
last_name = 'Olcar'  
message = first_name + ' [' + last_name + '] is a coder'
msg = f'{first_name} [{last_name}] is a coder'  
print(msg)  
print(message)
```

In this case when print command occurred both msg and message variables will have the same string values. 

******

Examples for **methods** in python: 

```python
course = 'python for beginners is here heheheh lol'
print(len(course))  
print(course.upper())  
print(course.lower())  
print(course)  
print(course.find('b'))  
print(course.replace('beginners','ABSOLUTE vodka'))
print('python' in course)
```

*********

**If, Elif, Else**
A simple program for identification for:
If an applicant has good or bad credit to calculate the down payment value and the final discounted price.

```python
price: int = 1000000  
buyer_credit = input('is your credit good')
if buyer_credit.lower() == 'yes':  
    print('20% decreased is')  
    down_payment = 0.2 * price  
elif buyer_credit.lower() == 'no':  
    print('10% decreased is')  
    down_payment = 0.1 * price  
print(f"price of the house is {price} $")
print(f"Payment: ${price - down_payment}")
```
1st Run:
```
is your credit good yes
20% decreased is
price of the house is 1000000 $
Payment: $800000.0
```
2nd Run:
```
is your credit good no
10% decreased is
price of the house is 1000000 $
Payment: $900000.0
```

*********

Logical Contitions:

- Or/ at least one true

```python
has_high_income = False  
has_good_credit = True 

if has_good_credit or has_high_income:
    print("Eligible for loan")
```
Run:
```
Eligible for loan
```

- And/ both are true

```
has_high_income = True  
has_good_credit = True

if has_good_credit and has_high_income:  
    print("Eligible for loan")
```
Run:
```
Eligible for loan
```

- Not/ inverses boolean values

```python
has_criminal_record = True  
has_good_credit = False  
  
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
```

```
Eligible for loan
```

*********

Comparison Conditions:
Used for making a boolean value at the end

```python
<   --->  smaller than
<=  --->  smaller than or equal to
>   --->  greter than
>=  --->  greater than or equal to
```

Note len() gives the number of characters in a strings

```python
name = input("Write a name: ")
if len(name) <= 3:  
    print('name must be at lest 3 characters long')
elif len(name) >= 50:  
    print("name can be a maximum of 50 characters")
else:  
    print("✓")
```
1st Run:
```
Write a name: yigit
✓
```
2nd Run:
```
Write a name: ttt
name must be at lest 3 characters long
```
3rd Run:
```
Write a name: ttttttttttttttttttttttttttttttttttttttttttttttttttt
name can be a maximum of 50 characters
```

*********


**While loops**
While loops are used for looping the code until a condition is reached:
As shown below variable `i` is equal to 1 at  first and a while loop is introduced which increases `i` one at a time until it reaches the final value of 5 and prints done at the end to show "loop is finished and is terminated" to the user.
```python
i = 1  
while i <= 5:  
    print(i)  
    i = i+1  
print('done')
```
Run:
```
1
2
3
4
5
done
```
Same thing can be made with replacing the integer with a string then string will be multiplied unit reaches the limit '5'
<br>
Then the terminal after the Run will look like:
```
*
**
***
****
*****
done
```

**********

For Loops
```python
for i in 'Pyhton':  
    print(i)
```


In for loop two variables are needed ``for `i` in `numbers`:`` i variable is used only in the loop for iterating the list given in the second variable, `numbers`.

For loops = execute a block of code a fixed number of times .
You can iterate over a range, string, sequence, list etc.

Shopping List Summation:
```python
prices = [10, 20, 30]  
total = 0  
for price in prices:  
    total = total + price  
print(f"Total:{total}")
```
Run
```
Total:60
```

*********

```python
sayilar = [20, 30, 60]  
sum = 0  
for sayi in sayilar:  
  sum = sum + sayi  
  print("Sayi:", sayi)  
  print("Sum:", sum)
```


```python
numbers = [1, 4, 9, 5, 8]  
max = numbers[0]  
for number in numbers:  
    if number > max:  
        max = number  
print(max)
```

```python
numbers = [3, 5, 8, 0, 79, 9, 4, 1, 7]  
max = numbers[0]  
for i in numbers:  
    if max < i:  
        max = i  
print(max)
```

*******

**Nested looops**
Loops that are inside one another
```python
for x in range(4):  
    for y in range(3):  
        print(f"({x}, {y})")
```
  
```python
numbers = [2, 2, 2, 2, 5]  
for x_count in numbers:  
    output = ''  
    for count in range(x_count):  
        output = output + 'x'  
    print(output)  

```

********
2D Lists
```python
matrix = [  
    [1, 2, 3],  
    [4, 5, 6],  
    [7, 8, 9]  
]  
for row in matrix:  
    for item in row:  
        print(item)
```

Run:
```
1
2
3
4
5
6
7
8
9
```

****************

```python
numbers.append(6)       # adds 6 to the end

numbers.insert(0, 6)    # adds 6 at index position of 0

numbers.remove(6)       # removes 6

numbers.pop()           # removes the last item

numbers.clear()         # removes all the items

numbers.index(8)        # returns the index of first occurrence of 8

numbers.sort()          # sorts the list

numbers.reverse()       # reverses the list

numbers.copy()          # returns a copy of the list
```

*********

```python
numbers = [1, 4, 9, 5, 8]  
print(50 in numbers)
```
Run
```
False
```

**********


```python
numbers = [1, 1, 2, 3, 4, 4, 5, 6, 6, 7, 7]  
unique = []  
for number in numbers:  
    if number not in unique:  
        unique.append(number)  
print(unique)
```
Or
```python
numbers = [1, 1, 2, 3, 4, 4, 5, 6, 6, 7, 7]  
numbers2 = numbers.copy()  
  
for number in numbers2:  
    if numbers.count(number) > 1:  
        numbers.remove(number)  
  
print(numbers)
```
Or
```python
numbers = [1, 1, 2, 3, 4, 4, 5, 6, 6, 7, 7]  
numbers2 = numbers.copy()  
  
for number in numbers2:  
    if number in numbers:  
        numbers.remove(number)  
  
print(numbers)
```
***********

```c
Tuples

They are like read only lists. We use them to store a list of items. But once we

define a tuple, we cannot add or remove items or change the existing items.

coordinates = (1, 2, 3)

We can unpack a list or a tuple into separate variables:

coordinates = (1, 2, 3)  
x = coordinates[0]  
y = coordinates[2]  
z = coordinates[3]  
  
x, y, z = coordinates

```


*********

Emoji Converter
```python
message = input(">")  
words = message.split(' ')  
emojis = {  
    ":)": "😃",  
    ":(": "😧"  
}  
output = ''  
for word in words:  
    output+= emojis.get(word, word) + " "  
    print(output)
```

**********

Functions
```python
def greet_user(first_name, last_name):  
    print(f'Hi there {first_name} {last_name}!')  
    print('Welcome aboard')  
  
  
print("Start")  
greet_user(last_name="bas", first_name="deniz")  
print("Finish")
```


Emoji Converter but this time making it a function to make that code reusable.
```python
def emoji_converter(message):  
    words = message.split(' ')  
    emojis = {  
        ":)": "😃",  
        ":(": "😧"  
    }  
    output = ''  
    for word in words:  
        output += emojis.get(word, word) + " "  
    return output  
  
  
message = input(">")  
print(emoji_converter(message))
```

*******
Managing errors

We use try and except in order to manage errors.
We don't want our code to crash, so we make some exceptions for it not to crash.
```python
try:  
    age = int(input('Age: '))  
    print(age)  
except ValueError:  
    print('Invalid Value!!!')
```

```python
try:  
    age = int(input('Age: '))  
    income = 20000  
    risk = income / age  
    print(age)  
except ValueError:  
    print('Invalid Value!!!')  
except ZeroDivisionError:  
    print('Age cannot be zero(0)')
```

**********

***Classes***

I talked about different types such as integers or boolean values floats etc. 
Class is how we define different types. For example a point in a two dimensional plane  is neither a boolean nor integer its just a point. Or same thing can be applied to a shopping cart a shopping cart is a shopping cart. 
With using **Classes** we can define what a point is. We use classes to define new types basically.
```python
class Point:  
    def move(self):  
        print('move')  
    def draw(self):  
        print('draw')  
  
point1 = Point()  
point1.x = 10  
point1.y = 20  
print(point1.x)  
  
point2 = Point()  
point2.x = 15  
point2.y = 25  
print(point2.x)  
  
point1.move()  
point1.draw()
```

Run
```
10
15
move
draw
```

******

Class Summay
```python
  
import math    # If we import a library such as math  
               # what we basically do is to import bunch of classes to our code but simplified  
  
print('What can do what?')  
class Mammal:  
    def walk(self):              # Functions defined inside of classes are called modules  
        print("Can walk")  
  
  
    def walk(self):  
        print("Can walk")  
  
class Dog(Mammal):  
    def bark(self):  
        print("Can Bark")  
  
class Cat(Mammal):  
    pass                         # Pass means noting it is there to indicate                                      # That it doesn't have anything in it  
                                 # Pass is basically there to pass the class

dog1 = Dog()  
print('Dog')  
dog1.walk()  
dog1.bark()  
  
cat1 = Cat()  
print('Cat')  
cat1.walk()
```

*******

**Modules**

A module is a file with some Python code. We use modules to break up our

program into multiple files. This way, our code will be better organized. We won’t

have one gigantic file with a million lines of code in it!

There are 2 ways to import modules: we can import the entire module, or specific

objects in a module.

```python
# importing the entire converters module

import converters

converters.kg_to_lbs(5)

# importing one function in the converters module

from converters import kg_to_lbs

kg_to_lbs(5)
```






************

in app.py file
```python
from utils import find_max  
  
numbers = [1, 42, 54, 40, 25]  
max_ = find_max(numbers)  
print(max_)
```


in utils.py file
```python
def find_max(numbers):  
    max_ = numbers[0]  
    for numbers in numbers:  
        if numbers > max_:  
            max_ = numbers  
    return max_
```


*******

**Packages**

A package is a directory with __init__.py in it. It can contain one or more modules.
```python
# importing the entire sales module

from ecommerce import sales

sales.calc_shipping()

# importing one function in the sales module

from ecommerce.sales import calc_shipping

calc_shipping()
```


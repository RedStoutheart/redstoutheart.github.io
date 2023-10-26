---
title: My Python Adventure
feed: show
date: 17-10-2023
---
*********
<font size="+3">This is the page that I will share my adventure along the way of learning python.
</font><br><br><br><br><br><br>
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

```c
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
```c
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

```c
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

```c
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

```c
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

```c
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

```c
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

```c
<   --->  smaller than
<=  --->  smaller than or equal to
>   --->  greter than
>=  --->  greater than or equal to
```

Note len() gives the number of characters in a strings

```c
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
```c
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


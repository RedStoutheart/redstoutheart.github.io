---
title: Simple Programs Made With Python
feed: show
date: 23-10-2023
---
In this page I will show you some examples for simple programs that i made along the way of learning python
<br><br><br><br><br><br>
**Weight converter**

```
weight = float(input('Weight: '))  
conv = input("(L)bs or (K)g: ") 

if conv.upper() == "K":  
    var = weight * 2.20  
    print(f"You are {var} pounds")  
  
elif conv.upper() == "L":  
    var = weight * 0.45  
    print(f"You are {var} kilos")  
  
else:  
    print("write K or L")

```
1st Run
```
Weight: 78
(L)bs or (K)g: l
You are 35.1 kilos
```
2nd Run
```
Weight: 31.1
(L)bs or (K)g: k
You are 68.42 pounds
```
3rd Run
```
Weight: 64
(L)bs or (K)g: x
Write K or L!
```

********
**Car Engine Game:**

```
command = ''  
s_tarted = False  
while True:  
    command = input('> ').lower()  
  
    if command == 'start':  
        if s_tarted:  
            print('Car is already started!')  
        else:  
            s_tarted = True  
            print('Car started...Ready to go!')  
  
    elif command == 'stop':  
        if not s_tarted:  
            print('Car is already stopped!')  
        else:  
            s_tarted = False  
            print('Car stopped.')  
  
    elif command == 'help':  
        print("""start - start the car  
stop - stop the car  
quit - to exit""")  
  
    elif command == 'quit':  
        break  
  
    else:  
        print("I don't understand that")  
  
print("\033[32;5m\n"  
      "THANK YOU FOR PLAYING")
      
```

Run
```
> ttt
I don't understand that
> help
start - start the car
stop - stop the car
quit - to exit
> start
Car started...Ready to go!
> stop
Car stopped.
> tart
I don't understand that
> start
Car started...Ready to go!
> start
Car is already started!
> stop
Car stopped.
> stop
Car is already stopped!
> quit

THANK YOU FOR PLAYING
```
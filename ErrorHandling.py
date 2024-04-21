Exception Handling

There are going to be times when your code tries to show up some errors or other problem inside the code that you are doing, and this is where the exception is going to occur.

Knowing when to recognize these exceptions, how to handle them, and even how to make some of your own can make a big difference in how well you are able to control your own coding in Python.
A good example of an exception that your compiler is automatically going to raise up is when you or the user is to divide it by zero. The compiler is then going to recognize that this is something the user is not able to do, and it is going to send out that exception as an alert.
It can also be something that is going to be called up if you, as the programmer, are trying to call up a function and the name is not spelled in the proper manner so there is no match present to bring up.

If you are going through some of the code writing, and you start to notice that an exception will be raised, know that often the solution is going to be a simple one. But as the programmer, you need to take the time to get this fixed

Built-in exceptions:
Finally-this is the action that you will want to use to perform cleanup actions, whether the exceptions occur or not. I
Assert this condition is going to trigger the exception inside of the code.
Raise the raise command is going to trigger an exception manually inside of the code.
• Try/except-this is when you want to try out a block of code and then it is recovered


Example 1:
# import module sys to get the type of exception import sys
randomList = ['a', 0, 2]
for entry in randomList:
try:
print("The entry is", entry) r = 1/int(entry)
break
except:
print("Oops!", sys.exc_info()[0], "occurred.") print("Next entry.")
print()
print("The reciprocal of" entru "ic" r)


import sys
randomList = ['a', 0, 2]
for entry in randomList:
try:
print("The entry is", entry) r = 1/int(entry)
break
except Exception as e:
print("Oops!", e. class, "occurred.") print("Next entry.")
print()
print("The reciprocal of", entry, "is", r)

#Example of Raising Error

try:
    print(1/0)
except:
    raise RuntimeError("Something Bad Happened")
    














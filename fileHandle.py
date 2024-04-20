File Handling:
When we want to read from or write to a file, we need to open it first. When we are done, it needs to be closed so that the resources that are tied with the file are freed.
In Python, a file operation takes place in the following order:
Open a file
Read or write (perform operation)
Close the file
Open a file
Python has a built-in open() function to open a file. This function returns a file object, also called a handle, as it is used to read or modify the file accordingly.
>>> f = open("test.txt") # open file in current directory
>>> f = open("C:/Python38/README.txt") # specifying full path
We can specify the mode while opening a file. In mode, we specify whether we want to read r, write w or append a to the file. We can also specify if we want to open the file in text mode or binary mode.
The default is reading mode. In this mode, we get strings when reading from the file.
On the other hand, binary mode returns bytes and this is the mode to be used when dealing with non- text files like images or executable files.
f = open("test.txt") # equivalent to 'r

f = open("test.txt",'w') # write in text mode
f= open("test.txt", mode='r', encoding='utf-8}

r        Opens so file for reading 
w        Opens a file for writing Creates a new does not exist or truncates the new file
x        Opens a tile for exclusive creation If the file steady exists, the operation foll
a         Opens a file for appending at the end of the file without trunooting it. Creates file if it does not exist.
t         Opens in text mode (default)
b         Opens in binary mode.
*         Opens a file for updating (reading and writing)

 Closing a file
 
When we are done with performing operations on the file, we need to properly close the file.

Closing a file will free up the resources that were tied with the file. It is done using the close() method available in Python.

Python has a garbage collector to clean up unreferenced objects but we must not rely on it to close the file.

f= open("test.txt", encoding = 'utf-8')

#perform file operations
f.close() I
This method is not entirely safe. If an exception occurs when we are performing some operation with the file, the code exits without closing the file. A safer way is to use a try...finally block  

try:
f= open("test.txt", encoding = 'utf-8')
#perform file operations
finally:
f.close()
This way, we are guaranteeing that the file is properly closed even if an exception is raised that causes program flow to stop. The best way to close a file is by using the with statement. This ensures that the





















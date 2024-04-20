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

        

#In python you can actually print using separator actually
str1="Hello"
str2="World"
print(str1,str2)
#Tuple is very much similiar to list the main difference is unlike list you cannot change the elements of tuple once it is set

aTuple=(1,3,5)
#Tuple of Different data Types
tupleData=("aTuple",1,2,3)

#Nested Tuples

nestedTuple=(1,"s",[5,4,3],[1,2])
#Tuple can be accesed very much like a list at least
#If we use [] to get the value but if the key does not exist it will return error whereas using get() method returns None if the key doesn't exist


When importing a module, the interpreter automatically searches the same module for its current address, if this is not available, Python (or its interpreter) will perform a search on the PYTHONPATH environment variable that is nothing more than a list containing directory names with the same syntax as the environment variable.
The Python interpreter searches the file system for the current directory where it is executed. Then, the interpreter searches for its predefined paths in its configuration.
When it meets the first match (the name of the module), the interpreter automatically executes it from start to finish.
When importing a module for the first time, Python will generate a compiled .pyc extension file. This extension file will be used in the following imports of this module.
When the interpreter detects that the module has already been modified since the last time it was generated, it will generate a new module.
You must save the imported file in the same directory where Python is using the import statement so that Python can find it.

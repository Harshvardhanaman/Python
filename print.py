# How Does the Computer Understand Python?
# Computer understands Machine Language made of 0s and 1s (tiny electrical switches turning OFF and ON).
# Compilation to Bytecode: Python first checks code for grammar mistakes (called Syntax Errors).
# If everything looks good, an internal compiler translates your code into a middle-level format called Bytecode (stored internally as .pyc).
# The CPU cannot run it directly either—it is a clean, optimized intermediate format.
# Execution by the PVM (Python Virtual Machine): 
# Inside Python lives an engine called the Python Virtual Machine (PVM). 
# It acts as the live interpreter—reading that Bytecode line by line from top to bottom and translating each instruction into 0s and 1s for your computer's CPU to execute.


# Basic text printing using double quotes and single quotes
print("Hello Stuti, How are you.") # str data type
print('You know python is a case sensitive language') # str data type

# Printing numbers vs printing text that looks like numbers
print(500)
print(500 + 844) # This is a number (int data type)
print("500 + 844") # This is not a number its a string because it covers with double quotes. (str data type)

# Printing multiple items in a single print command using commas
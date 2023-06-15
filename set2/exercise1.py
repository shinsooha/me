"""
Commenting skills:

NOTE: this file runs just fine, this is for you to learn to use the debugger!

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# This line imports the 'platform' module.
# It allows you to access information about the underlying platform (operating system, hardware, etc.). 

# I think this will print "hello! Let's get started" by calling the print function.
print ("hello! Let's get started") 
# This line prints the string "hello! Let's get started" to the console 
# When executed, it will display the text as output.

some_words = ["what", "does", "this", "line", "do", "?"]
# This line creates a list named 'some_words' containing several string elements.

# I think this will print "word" by calling the print function 
for word in some_words:
    print(word)
# This loop iterates over each element in the 'some_words' list.
# On each iteration, it prints the value of 'word', which represents the current element.

for x in some_words:
    print(x)
# This loop is similar to the previous one but uses a different variable name 'x' instead of 'word'.
# It also iterates over each element in the 'some_words' list and prints the value of 'x'.

print(some_words)
# This line prints the entire 'some_words' list.
# When executed, it will display the list as output.

if len(some_words) > 3:
    print("some_words contains more than 3 words")
# This 'if' statement checks whether the length of the 'some_words' list is greater than 3.
# If it is, it will print the string "some_words contains more than 3 words".

def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())
# This is a function named 'usefulFunction'.
# It prints the information obtained from the 'platform.uname()' function, which provides details about the system.

usefulFunction()
# This line calls the 'usefulFunction' and executes its code.
# When executed, it will print the system information using the 'platform.uname()' function.
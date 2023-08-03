
Debbuging:

Coding consists of 3 steps:
- Writing
- Executing (or running)
- Fixing errors (or debugging) 

In this lesson, you'll start step 3: identifying and fixing errors.

The code below contains an error. Python will return an error message. "Run" the code to get the error message.

message = "Debugging ~~ falta "
print(message)

The computer reads and executes instructions line by line, from top to bottom. The execution of the program will be interrupted at the first error encountered.
_________________________________________________________________

Standards and Best Practices:

You can add comments to your Python code with the hash symbol #

#Displaying a message
print("Insufficient funds")

Python is a case-sensitive language.
You can get errors if you don't pay attention to the use of uppercase and lowercase.

Snake case is a popular way to create variable names in a consistent way. Snake case uses underscores _ to separate words in a variable name.
Exemplo: dog_name
__________________________________________________________________

Inputs and Outputs:

An input is any information that goes into a computer.
The press of a key and the click of a button are examples of inputs.

The input() instruction is the easiest way to allow a user to insert a value into your program.
message = input()
print(message)

An output is a way for the computer to communicate with the outside world. A message displayed on the screen and the sound from a speaker are examples of outputs.
Example: a document goig out of a printer
____________________________________________________________________

Data Types:

Data comes in different shapes and forms. Computers treat different types of data in different ways.
- string --> entre "" ou ''
- float e int

The way computers operate with values depends on the data type.
print(3 + 5) 
print("Iron" + "Man")

When you use the + addition operator with string values the two strings are joined together. 
This is known as concatenation.
print("360" + "360") ---> 360360

name="Ann"
message="Hello, " + name
print(message)
____________________________________________________________________________

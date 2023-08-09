Data comes in a variety of shapes and forms. Dealing with data in the incorrect format can result in data loss or corruption. 

- string
- int 
- float

a = "note"
b = "book"
print(a+b)

The code below will result in an error. You can't add a number to a string. 

a = 3
b = "8"
print(a + b)

What will this code output?

balance = 234.3
print(type(balance)) #<class 'float'> , também tem 'str' e 'int'

The division of two integers always produces a float.

a = 4
b = 2
c = 4/2

The input() instruction always turns the user input into a string, no matter what the user enters.
 
birth_year = input()
print(type(birth_year))

The int() instruction converts any type of value into an integer

x = "55" #x is a string
y = int(x) #y is an integer

The int(), str() and float() instructions are examples of explicit conversion, which means they are performed by an instruction given by a programmer (like you).

On the other hand, run the code to see some examples of implicit (automatic) data type conversions

x = 5 # integer
y = 2 # integer

z = x/y # float (implicit conversion)

What will the code output?

x = input()
y = input()
print(x+y) #the concatenation of two strings

Exemplo:
# Asks the user to enter the savings
savings = input()

# Convert the user input into a float value and update the variable
savings = float(savings)

# Savings grow after 1 year at a 5% annual interest rate
balance = savings * 1.05 

# Convert the balance into a string and update the variable
balance = str(balance)

Math operations between integers and floats produce a float.

What will the code display on the screen?
x = 9
y = 3.0
print(x+y) #12.0

# Concatenate the 2 strings to produce a message
message = "Amount in 1 year: " + balance

# Display the message
print(message)

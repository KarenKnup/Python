Comparison operations are key to the development of computer programs. The line of code below shows an example of a comparison operation.

5 < 9 #True
50 > 100 #False
print(30 < 25)

Electronic circuits inside computers use millions of tiny switches to store these True/False values.
How many possible positions do these switches have? #ON/OFF

Computers use binary code to represent information. By turning switches ON and OFF, we change the information stored in a computer.
What does binary mean in this context? #two possibilities for the state of a switch

To simplify things, two numbers are used to represent the OFF/ON states of a switch. These numbers are: 0 and 1

Complete the code with the comparison operator that will make the code output the True value:

soil_moisture = 80
soil_moisture = 120
print(soil_moisture < 100) #False

Modern computers can perform complex tasks very fast because these can be broken down into lots of tiny, simple calculations.

Logical operations are needed for machines to evaluate complex scenarios. Logical operations use Boolean values. 
  
A logical operation takes several Boolean inputs and produces only 1 Boolean output

The "and" operation results in a True value only when all the inputs are True at the same time. What’s the result of this "and" logical operation?

True and True #True
True and False #False

The "or" logical operation results in a True value if at least one of the inputs is True. What’s the result of this "or" logical operation?

True or False #True
False or False #False

Logical operations need to be inserted in print() instructions for the result to be outputted.

print(True and False)
print(False and True)
print(True or False)
print(False or True)

The smartwatch can detect when the user is sleeping. Complete the code to store the boolean into the variable

sleep = True

You can store the result of a comparison operation as a variable.

heart_rate = 165
peak_rate = heart_rate > 160

Python is a case-sensitive language. 
- Both "True" and "False" start with an uppercase letter.
- Both "and" and "or" operators are lowercase in Python. 

light_on = True
door_locked = False
print(light_on or door_locked)
print(light_on and door_locked)

The temperature control system should only turn on the air-conditioning when the temperature is greater than 30 °C and there are people in the house.
Make the following operation result in True under these conditions

presence and (temp > 30)

Exemplo:
# Take steps and minutes as inputs
steps = int(input())
active_minutes = int(input())

# Store the result of the operations in the variable
goal_achieved = (steps > 10000) or (active_minutes > 30)

# Display the result on the screen
print(goal_achieved)

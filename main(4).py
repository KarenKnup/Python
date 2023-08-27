You already know ''sequencing''. It means that the computer runs your code in order, from top to bottom.

''Iteration'' is about executing an instruction repeatedly. Iteration is commonly represented as a loop.

''Selection'' specifies when to follow each path.

An algorithm is a set of step-by-step instructions to complete a task, placed in a certain order.

Another way to represent an algorithm is with pseudocode. Pseudocode is a simplified language that is a bit closer to a programming language.
  start
  repeat until authorised = true
  	INPUT log_in
  access_granted = true
_________________________________________________
A "for" loop is used to execute the same instruction over and over again, a specific number of times.

# Message to be displayed
message = "Fasten your seat belt"

# for loop to display the message 3 times
for i in range(3):
   print (message)
__________________________________________________
  "While" loops are powerful because they can be used even when you don’t know how many iterations will be needed.

  # take the number as input
number = int(input())

  #use a while loop for the countdown
while number >= 0:
   print(number)
   number = number - 1
___________________________________________________

The Goodbye message will only be displayed once. Why? The lack of indentation shows that the statement is outside the loop

for i in range(5):
  print("Hello")
print("Goodbye")
_____________________________________________________

age = 22
if age >= 18:
  print("Regular price")
else:
  print("Discount")
_____________________________________________________
# Take the number of available spaces as an input
spaces = int(input())

# Display message if spaces are available
if spaces <= 20 and spaces != 0:
    print("Available spaces")

# Display a different message if spaces are not available
if spaces == 0:
    print("Sorry, the parking lot is full")
_____________________________________________________
  if age < 18: 
  print("Junior discount")
elif age >= 75: 
  print("Senior discount")
else:
  print("No discount")
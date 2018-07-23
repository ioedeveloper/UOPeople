#Prompt for first number 
prompt = input("Enter First Number ")

#Read first number and store in variable 
firstnumber = int(prompt)

#While first number is equal to 0 display error
while(firstnumber == 0):
    print("Error: first number cannot be 0")
    prompt = input("Enter First Number ")
    firstnumber = int(prompt)

#Prompt for operation
prompt = input("1-add, 2-subtract, 3-multiply, 4-divide ")

#Read operation and store in variable 
operation = int(prompt)

#While operation is equal to less than 1 or greater than 4 display error
while(operation < 1 or operation > 4):
    print("Error: No operation found for "+prompt)
    prompt = input("1-add, 2-subtract, 3-multiply, 4-divide ")
    operation = int(prompt)

#Prompt for second number 
prompt = input("Enter Second Number ")

#Read second number and store in variable 
secondnumber = int(prompt)

#While second number is equal to 0 display error
while(secondnumber == 0):
    print("Error: Second number cannot be 0")
    prompt = input("Enter Second Number ")
    secondnumber = int(prompt)

#If operation is equal to 1 add firstnumber to secondnumber
if(operation == 1):
    result = firstnumber + secondnumber

#If operation is equal to 2 subtract secondnumber from firstnumber
elif(operation == 2):
    result = firstnumber - secondnumber

#If operation is equal to 3 divide firstnumber by secondnumber
elif(operation == 3):
    result = firstnumber * secondnumber

#If operation is equal to 4 divide firstnumber by secondnumber
elif(operation == 4):
    result = firstnumber / secondnumber

#Print result of operation
print (result)


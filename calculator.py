print("Welcome to my calculator")
print("Select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

#Asking for user input
choice = input("Enter your choice (1/2/3/4): ")

print("You selected:", choice)

if choice =="1":
    print("You chose Addition")

elif choice == "2":
    print("You chose subtraction")

elif choice =="3":
    print("You chose Multiplication")

elif choice =="4":
    print("You chose Divition")

else:
    print("Invalid choice")

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

num1 = float(num1)
num2= float(num2)


try:
   print("First number:", num1)
   print("second number:", num2)
except ValueError:
    print("Please enter valid numbers")
    
if choice == "1":
    result = num1 + num2
    print (f"Result: {num1} + {num2} = {result}")

elif choice == "2":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

elif choice == "3":
    result =  num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: You cannot divide by zero!")
else:
    print("Invalid operation choice.")


# Display a welcome message to the user
print("Welcome to my calculator")

# Show the available operations
print("Select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

# Asking the user to choose an operation
choice = input("Enter your choice (1/2/3/4): ")

# Display the selected choice
print("You selected:", choice)

# Check which operation the user selected
if choice == "1":
    print("You chose Addition")

elif choice == "2":
    print("You chose subtraction")

elif choice == "3":
    print("You chose Multiplication")

elif choice == "4":
    print("You chose Divition")

else:
    # Handle invalid menu choices
    print("Invalid choice")

# Ask the user to enter two numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Convert the input values to floating-point numbers
num1 = float(num1)
num2 = float(num2)

# Try to display the numbers (error handling section)
try:
   print("First number:", num1)
   print("second number:", num2)
except ValueError:
    # This runs if the conversion to float fails
    print("Please enter valid numbers")
    
# Perform addition if choice is 1
if choice == "1":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

# Perform subtraction if choice is 2
elif choice == "2":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

# Perform multiplication if choice is 3
elif choice == "3":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

# Perform division if choice is 4
elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        # Prevent division by zero
        print("Error: You cannot divide by zero!")
else:
    # Handle invalid operation choices
    print("Invalid operation choice.")



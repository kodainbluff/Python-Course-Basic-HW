print("This program works as a simple calculator. You can enter 2 numbers and choose an action that should occur.")
num1 = int(input("Please input first number: "))
num2 = int(input("Please input your second number: "))
action = (input("Please choose an action: "))

allowedActions = {"/","+", "-", "*"}

if action not in allowedActions:
    print("Incorrect action.")


if action == "/":
    if num2 == 0:
        print("You cant divide by zero.")
    else:
        print(f"You chose those numbers: {num1}, {num2}. You chose this action: {action}. The answer to your equation is:", num1 / num2 )
elif action == "+":
    print(f"You chose those numbers: {num1}, {num2}. You chose this action: {action}. The answer to your equation is:", num1 + num2 )
elif action == "-":
    print(f"You chose those numbers: {num1}, {num2}. You chose this action: {action}. The answer to your equation is:", num1 - num2 )
elif action == "*":
    print(f"You chose those numbers: {num1}, {num2}. You chose this action: {action}. The answer to your equation is:", num1 * num2 )

input("Press any key to exit.")
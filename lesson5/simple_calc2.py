
print("This is an upgraded version of previous programm, that allows you continuously make simple arithmetic equations.")
usage = True

allowedActions = {"/","+", "-", "*"}


while usage == True:
    num1 = int(input("Please input first number: "))
    num2 = int(input("Please input your second number: "))
    action = (input("Please choose an action: "))
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
    continuation = input("Do you wish to use calculator again? If so press 'Y', if you want to exit press 'N'. ")
    if continuation == "Y":
         continue
    elif continuation == "N":
         usage == False
         break
    else: print("Unknown input")  
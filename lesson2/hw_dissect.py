print("This program will dissect the 4-digit number you enter, and show its numbers in a column")
number = int(input("Please enter a 4-digit number: "))
digit1 = number // 1000
digit2 = number % 1000 // 100
digit3 = number % 1000 % 100 // 10
digit4 = number % 1000 % 100 % 10
print(f"You have entered the next 4-digit number: {number}. Here is a column of the digits composing that number: \n{digit1}\n{digit2}\n{digit3}\n{digit4}")
input("Press any key to exit")
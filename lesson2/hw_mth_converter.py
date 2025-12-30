print("This program will convert minutes into hours.")
minutes1 = int(input("Please enter the amount of minutes you want to convert: "))
minutes2 = minutes1 % 60
hours1 = minutes1 // 60
print(f"You have entered this amount of minutes: {minutes1}. Converted time is: {hours1} hours and {minutes2} minutes.")
input("Press any key to exit.")

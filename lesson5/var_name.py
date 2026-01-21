#This programm will check if the entered string would work as a variable name
import string
import keyword

test_var = str(input("Please enter the name of a variable: "))

test_progress = []
counter = 0

if test_var[0].isdigit():
    test_progress.append(False)


for char in test_var:
    if char.isupper():
        test_progress.append(False)
        break
    if char in string.punctuation:
        if char == "_":
            pass
        else:
            test_progress.append(False)
            break
    if char == "_":
        counter += 1
        if counter >= 2:
            test_progress.append(False)
            break
    if char.isspace():
        test_progress.append(False)
        break
    

if test_var in keyword.kwlist:
    test_progress.append(False)

if len(test_progress) == 0:
    print(f"The chosen variable '{test_var}' is usable")
else:
    print(f"The chosen variable {test_var} is not usable") 


print(test_progress)
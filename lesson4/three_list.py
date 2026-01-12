#This program will generate random list with 3 to 10 elements in it.
#It will then create a new list with first, third and second last elements from original list.
import random
list = []
list_len = random.randint(3, 10)
print(f"The length of this random list will be: {list_len}")

while list_len > 0:
    list.insert(-1, random.randint(0, 99))
    list_len = list_len - 1

print(f"The generated list is: {list}")
new_list = [list[1], list[3], list[-2]]
print(f"New list consisting of 1st, 3rd and 2nd last elements is: {new_list}")
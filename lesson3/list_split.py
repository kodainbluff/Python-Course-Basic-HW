#This programm will split a list in half
list1 = [1, 2, 3, 4, 5]
print(f"List before the changes: {list1}.")
slice1 = list1[:len(list1) // 2]
slice2 = list1[len(list1) // 2:]
list2 = [slice1, slice2]
print(f"List after the changes: {list2}")
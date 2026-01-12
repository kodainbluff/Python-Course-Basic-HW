#This programm will transfer the last item in a list to the 1st position without changing the order of the list

list = [12, 3, 4, 10]
print(f"List before the changes: {list}")
if len(list) == 0:
    print(f"The list is empty, no changes have been made. {list}")
else:
    last_item1 = list.pop()
    list.insert(0, last_item1)
    print(f"List after the changes{list}")


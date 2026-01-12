#This programm will transfer all zero integers to the beginning of the list
list = [0, 1, 0, 12, 3]
print(f"Original list: {list}")
new_list = []
counter = 0
for elem in list:
    if elem == 0:
        new_list.append(elem)
    else:
        counter += 1
        new_list.insert(0, elem)
new_list[0: counter] = new_list[0: counter][::-1]
print(f"New list: {new_list}") 


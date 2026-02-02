def unique_number(user_list):
    unique_number = [num for num in user_list if user_list.count(num) == 1]
    return unique_number[0]
    
assert unique_number([1, 2, 1, 1]) == 2, 'Test1'
assert  unique_number([2, 3, 3, 3, 5, 5]) == 2, 'Test2' 
assert unique_number([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3' 
print("ОК")
def add_one(user_list):
    num1 = int(''.join(map(str,user_list)))
    num2 = num1 + 1
    return [int(digit) for digit in str(num2)]
    
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1' 
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2' 
assert add_one([0]) == [1], 'Test3' 
assert add_one([9]) == [1, 0], 'Test4' 
print("ОК")

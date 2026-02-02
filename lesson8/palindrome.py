def palindrome(user_string):
    clean_string = "".join(char for char in user_string if char.isalnum())
    clean_string = clean_string.lower()
    return clean_string == clean_string[::-1]
    
assert palindrome('A man, a plan, a canal: Panama') == True, 'Test1' 
assert palindrome('0P') == False, 'Test2' 
assert palindrome('a.') == True, 'Test3' 
assert palindrome('aurora') == False, 'Test4' 
print("ОК")
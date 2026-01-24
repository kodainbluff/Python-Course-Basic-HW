def second_instance(text, letter):
    first_occurrence = text.find(letter)
    if first_occurrence != -1:
        output = text.find(letter, first_occurrence + 1)
        if output != -1:
            return output
        else:
            return "Second instance of this pattern is not found"
    else:
         return "Second instance of this pattern is not found"
assert second_instance("sims", "s") == 3, 'Test1' 
assert second_instance("find the river", "e") == 12, 'Test2' 
assert second_instance("hi", "h") == "Second instance of this pattern is not found", 'Test3' 
assert second_instance("Hello, hello", "lo") == 10, 'Test4' 
print("OK")
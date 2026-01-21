#This program will fill the provided range of letters with letters of english alphabet
import string

usable_letters = string.ascii_letters

user_input = input("Please type in the range of letters, e.g. a-z: ")
letter_range = list(user_input)
letter1 = user_input[0]
letter2 = user_input[-1]

range_start = usable_letters.index(letter1)
range_finish = usable_letters.index(letter2)

output = usable_letters[range_start : range_finish +1]

print(output)


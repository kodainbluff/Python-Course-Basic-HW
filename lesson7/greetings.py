def greetings(name, age):
     return f"Hello, my name is {name}. I am {age} years old"

assert greetings("Alex", 32) == "Hello, my name is Alex. I am 32 years old", 'assert_test1'
assert greetings("Quasimodo", 1000) == "Hello, my name is Quasimodo. I am 1000 years old", 'assert_test2'

print("OK")

print(greetings("Alex", 32))
print(greetings("Frank", 44))
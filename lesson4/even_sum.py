#This porgramm will summ even elements in a list, and then multiply the sum by a last digit in a list
try:
    list = []
    print(f"Original list: {list}")
    list_sum = sum(list[::2])
    result = list_sum * list[-1]
except Exception as e:
    print(f"There was an error: {e}.")
    result = 0
finally:
    print(f"The resul of our operations is: {result}")
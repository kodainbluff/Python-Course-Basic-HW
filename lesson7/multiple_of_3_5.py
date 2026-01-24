def common_elements():
    multiple3 = set(range(0, 100, 3))
    multiple5 = set(range(0, 100, 5))
    output = multiple3.intersection(multiple5)
    return output
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")
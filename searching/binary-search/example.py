from binary_search import binary_search

numbers = [1, 3, 5, 7, 9, 11, 14]
target = 9
result = binary_search(numbers, target)

if result != -1:
    print(f"Found at index {result}")
else:
    print("Not found")
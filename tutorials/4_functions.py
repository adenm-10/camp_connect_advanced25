"""Example Using Functions"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Swap if the current element is greater than the next
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

num1 = [5, 1, 4, 2, 8]
num2 = [6, 3, 10, 1, 2]
num3 = [2, 3, 1, 8, 4]

print(bubble_sort(num1))  # Output: [1, 2, 4, 5, 8]
print(bubble_sort(num2))  # Output: [1, 2, 3, 6, 10]
print(bubble_sort(num3))  # Output: [1, 2, 3, 4, 8]


"""Example not using Functions"""
arr = [5, 1, 4, 2, 8]
n = len(arr)
for i in range(n):
    # Last i elements are already sorted
    for j in range(0, n - i - 1):
        # Swap if the current element is greater than the next
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)  # Output: [1, 2, 4, 5, 8]

arr = [6, 3, 10, 1, 2]
n = len(arr)
for i in range(n):
    # Last i elements are already sorted
    for j in range(0, n - i - 1):
        # Swap if the current element is greater than the next
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)  # Output: [1, 2, 3, 6, 10]

arr = [2, 3, 1, 8, 4]
n = len(arr)
for i in range(n):
    # Last i elements are already sorted
    for j in range(0, n - i - 1):
        # Swap if the current element is greater than the next
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)  # Output: [1, 2, 3, 4, 8]

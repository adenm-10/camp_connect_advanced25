def isOdd(num: int):
    return num % 1 == 1

def sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Swap if the current element is greater than the next
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage
nums = [5, 1, 4, 2, 8]
sorted_nums = sort(nums)
print(sorted_nums)  # Output: [1, 2, 4, 5, 8]

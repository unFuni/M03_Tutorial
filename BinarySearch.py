def binarySearch(arr, n):
    min = 0
    max = len(arr)  - 1

    while min <= max:
        mid = min + (max - min) // 2

        if arr[mid] == n:
            return mid
        elif n > arr[mid]:
            min = mid + 1
        else:
            max = mid - 1

        if arr[mid + 1] == n:
            return mid + 1
        elif arr[mid - 1] == n:
            return mid - 1
    
    return  -1

k = 4

input = [1, 2, 3, 4, 5]

n = binarySearch(input, k)

print("Output: " + n.__str__())
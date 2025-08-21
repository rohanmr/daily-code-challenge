arr=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

def trap_water_two_pointers(arr):
    n = len(arr)
    if n == 0:
        return 0

    i, j = 0, n - 1

    left_max, right_max = 0, 0
    total = 0

    while i < j:
       
        left_max = max(left_max, arr[i])
        right_max = max(right_max, arr[j])

       
        if left_max <= right_max:
            total += left_max - arr[i] 
            i += 1
        else:
            total += right_max - arr[j]
            j -= 1

    return total


x=trap_water_two_pointers(arr)
print(x)
arr=[3,1,3,4,2]

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] == arr[j]:
            print(arr[i])
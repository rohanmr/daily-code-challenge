arr = [0, 1, 2, 1, 0, 2, 1, 0]

def sortArray(arr):
    n=len(arr)
    
    for i in range(n):
        mini=i
        for j in range(i+1,n):
            if arr[mini] > arr[j]:
                mini=j
        
        arr[i],arr[mini]=arr[mini],arr[i]

sortArray(arr)
print(arr)






    
    
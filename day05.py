arr=[16,17,4,3,5,2]

def findLeaderElement(arr):
    n=len(arr)
    leadersArr=[]
    for i in range(n):
        isleader=True
        for j in range(i+1,n):
            if arr[i] < arr[j]:
                isleader=False
                break
        if isleader:
            leadersArr.append(arr[i])
    
    return leadersArr

    
result=findLeaderElement(arr)
print(result)




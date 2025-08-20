arr=[1, 2, -3, 3, -1, 2]

def findSubArry(arr):
    n=len(arr)
    subArry=[]

    for i in range(n):
        total=0 
        for j in range(i,n):
            total+=arr[j]

            if total == 0:
               subArry.append((i,j))
    

    return subArry

result=findSubArry(arr)
print(result)
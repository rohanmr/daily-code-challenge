arr=[1,0,2,1,2,1,0,1]

def SortArry(arr):
    n=len(arr)

    for i in range(n):
        mini=i  
        for j in range(i+1,n):
            if arr[mini]>arr[j]:
                mini=j 

        arr[mini],arr[i]=arr[i],arr[mini] 
             


SortArry(arr)
print(arr)



        
    
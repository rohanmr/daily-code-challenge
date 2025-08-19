arr1=[1,3,5,7]
arr2=[2,4,6,8]


def sortedArrayMerge(arr1,arr2):
    new=[]

    i,j=0,0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            new.append(arr1[i])
            i+=1
        else:
            new.append(arr2[j])
            j+=1
    
    new.extend(arr1[i:])
    new.extend(arr2[j:])

    return new

sorted_arr=sortedArrayMerge(arr1,arr2)

mid=len(sorted_arr)//2

print(sorted_arr[:mid])
print(sorted_arr[mid:])
s=input("enter string:")
k=int(input("Enter the k value:"))
n = len(s)
count = 0
    
    
for i in range(n):
        
    distinct_chars = set()
        
    for j in range(i, n):
           
        distinct_chars.add(s[j])
            
           
        if len(distinct_chars) == k:
            count += 1
           
        elif len(distinct_chars) > k:
            break
    
print(count)
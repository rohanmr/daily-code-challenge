strs =  ["apple", "ape", "april"]


prefix = strs[0]

for i in strs[1:]:
   
    while not i.startswith(prefix):
        prefix = prefix[:-1]  
        if prefix == "":
            break

print("Longest Common Prefix:", prefix)

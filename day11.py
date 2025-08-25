from itertools import permutations

def string_permutations(s: str):
    
    perms = permutations(s)
    
    unique = set("".join(p) for p in perms)
    
    return list(unique)


print(string_permutations("abc"))  
  

def string_palindrome(s: str) -> str:
    n = len(s)
    
    best = s[0]

    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            
            if substring == substring[::-1]:
               
                if len(substring) > len(best):
                    best = substring
    return best



print(string_palindrome("babad"))  


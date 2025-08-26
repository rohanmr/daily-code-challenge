s=input("Enter the string")

def valid_parentheses(s: str):
    while "()" in s or "{}" in s or "[]" in s:
        s = s.replace("()", "").replace("{}", "").replace("[]", "")
    return s == ""


result=valid_parentheses(s)

print(result)
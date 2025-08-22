str=input("Enter the string:")


x=str.split(" ")

res=x[::-1]

for i in res:
    print(i,end=" ")


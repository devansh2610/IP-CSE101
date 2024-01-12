n=int(input("enter n:"))

for i in range(1,n+1):
    for f in range(1,i+1):
        print("*",end="")
    for j in range(i+1,n+1):
        print(" ",end="")
    for m in range(i+1,n+1):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    print()


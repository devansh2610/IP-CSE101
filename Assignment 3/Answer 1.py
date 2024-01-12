x=int(input("Enter x: "))
y=x

def upper(n):
    if n<1:
        return
    else:
        if n==y:
            print("* "*(2*y))
        else:
            print("* "*n,end="")    
            print("  "*(2*y - 2*n),end="")
            print("* "*n)
        upper(n-1)

def lower(n):
    if n>y:
        return
    else:
        if n==2:
            print("* "*(n),end="")
            print("  "*(2*y - 2*n),end="")
            print("* "*n)
        if n>2:
            if n!=y:
                print("* "*n,end="")
                print("  "*(2*y - 2*n),end="")
                print("* "*n)
            if n==y:
                print("* "*(2*y))
        lower(n+1)

        
upper(x)
lower(y-(x-1))
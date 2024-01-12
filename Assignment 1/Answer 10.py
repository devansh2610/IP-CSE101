a= 1
b= -10.5
c= 34.5
d= -35

def p(x):
    z = a*(x**3) + b*(x**2) + c*x + d
    return z

def pdash(x):
    derivative = (a*3)*(x**2) + (b*2)*x + c
    return derivative

def func(p,x):
    P=p(x)
    return P

x0=float(input("enter x0: "))
i=x0
count=0
found=0

while True:
    count=count+1
    if count==101 and found<1:
        print("No closest approximate or exact root found within 100 tries")
        break
    else:
        if func(p,i)<=0.2 and func(p,i)>= -0.2:
            found=found+1
            print(f'{round(i,1)} is the root')
            break

    i= i - (p(i))/(pdash(i))




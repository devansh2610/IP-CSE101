def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def sin(x):
    sine=x
    flag=True
    for i in range(3,8,2):
        if flag:
            sine=sine - (((x)**(i))/(factorial(i)))
        else:
            sine=sine + (((x)**(i))/(factorial(i)))
        flag=not flag
    return sine

def cos(x):
    cosine=1
    flag=True
    for i in range(2,7,2):
        if flag:
            cosine=cosine - (((x)**(i))/(factorial(i)))
        else:
            cosine=cosine + (((x)**(i))/(factorial(i)))
        flag= not flag
    return cosine

def tan(x):
    tangent=(sin(x))/(cos(x))
    return(tangent)

a=int(input("enter angle in degrees: "))
b=int(input("enter horizontal distance:"))
a=a*((3.14)/180)                                    #converting angle to radians

height=tan(a) * b
hypotenuse=height/(sin(a))

print(f'Height of the pole is {height}')
print(f'Distance to the tip of the pole is {hypotenuse}')










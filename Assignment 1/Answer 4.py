import math
a=float(input("enter a:"))
b=float(input("enter b:"))
delta=0.25

def f(t):
    logn=math.log((140000)/((140000)-((2100)*t)))
    velocity= 2000*logn - 9.8*t
    return velocity

distance=0

while True:
    velo=f(a)+f((a+delta))
    velo=velo/2
    distance=distance + (velo*(delta))
    a=a+delta
    if a>=b:
        break

print(f"Total distance is {distance}")
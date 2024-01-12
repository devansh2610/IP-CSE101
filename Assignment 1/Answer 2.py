def const1(x1,x2):
    constraint1=8*x1 + 2*x2
    return constraint1

def const2(x1,x2):
    constraint2=2*x1 + 1*x2
    return constraint2

def objfunc(x1,x2,M):
    z=100*(x1-M) + 30*(x2-M) + 90*M + 25*M 
    return z

x=0
y=0
while True:
    Eq1=8*x + 2*y
    Eq2=2*x + 1*y
    if Eq1==400 and Eq2==120:
        n=x
        m=y
        break
    x=x+1
    y=y+1

list1=[]
for x in range(0,n+1):
    for y in range(0,m+1):
        if const1(x,y)<=400 and const2(x,y)<=120:
            p=objfunc(x,y,M=0)
            list1.append(p)
maximum=max(list1)

print(f'Maximum possible profit is {maximum}  (when M=0)')
print(f'Maximum number of tables is {n}')
print(f'Maximum number of tables is {m}')

M=10
profit=objfunc(x,y,M)
print(f'For M={M}, profit is {profit}')


M=int(input("enter M:"))
profit=objfunc(x,y,M)
print(f'For M={M}, profit is {profit}')



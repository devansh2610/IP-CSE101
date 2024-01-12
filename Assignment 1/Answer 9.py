e=2.718281828459045
def D(p):
    Qd = e**(a-b*p)
    return Qd
def S(p):
    Qs = e**(c+d*p)
    return Qs

price=1.0
a=10
b=1.05
c=1
d=1.06

i=0
m=0
while True:
    if m<1 and i==500:
        print("No equilibrium found within 500 tries")
        break
    else:
        Demand=round(D(price),1)
        Supply=round(S(price),1)
        if Demand-Supply<=round(0,2):
            print(f"Equilbrium price is {price}")
            print(f'Quantity demanded is: {D(price)}')
            print(f'Quantity supplied is {S(price)}')
            m=m+1
            break
        else:
            price = price + ((5/100)*price)
        i=i+1





    
        
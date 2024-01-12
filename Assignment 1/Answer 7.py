def laptop(cost,allowance=20000,sf=0.1,r=0.5):
    count=1
    savingsac=allowance*sf

    while savingsac<cost:
        savingsac=savingsac + (savingsac*(r/100)) + allowance*sf
        count=count+1

    print(f'You will be able to purchase the laptop after {count} months')
    print(f'Amount remaining after the purchase: {savingsac-cost}')


cost=int(input("enter cost:"))

laptop(cost)
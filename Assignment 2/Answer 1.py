menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]
print(menu)
l=[]
count=0
totprice=0
while True:
    order=input("Input order: ")
    if order=="":
        for i in l:
            for k in range(len(i)):
                if k<2:
                    print(i[k], end=", ")
                if k==2:
                    print(i[k])
        print(f'TOTAL, {count} items, Rs.{totprice}')
        break
    else:
        list1=order.split()
        if not(1<=int(list1[0])<=8):
            print("Enter a valid item number (from 1 to 8)")
            list1.pop(-1)
        else:
            if not(int(list1[1])>0):
                print("Enter a quantity greater than 0")
                list1.pop(-1)
            else:
                item=menu[int(list1[0]) - 1] 
                quant=int(list1[1])
                count=count+quant
                price=quant*item[1]
                totprice=totprice + price
                l.append((item[0],quant,"Rs." + str(price)))









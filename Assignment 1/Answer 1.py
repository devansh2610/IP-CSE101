d={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
d1={10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
dstring={'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
x=int(input('enter number:'))
x=str(x)                       #used in elif code block when int(x) in range(20,100)

if int(x) in range(0,10):
    for dkey,dvalue in d.items():
        if int(x)==dkey:
            print(dvalue)
elif int(x) in range(10,20):
    for d1key,d1value in d1.items():
        if int(x)==d1key:
            print(d1value)
elif int(x) in range(20,100):
    for key,value in dstring.items():
        if x[1]==str(key):
            m=value
    if x[0]=='2' and m=='zero':
        print('twenty')
    elif x[0]=='3' and m=='zero':
        print('thrity')
    elif x[0]=='4' and m=='zero':
        print('forty')
    elif x[0]=='5' and m=='zero':
        print('fifty')
    elif x[0]=='6' and m=='zero':
        print('sixty')
    elif x[0]=='7' and m=='zero':
        print('seventy')
    elif x[0]=='8' and m=='zero':
        print('eighty')
    elif x[0]=='9' and m=='zero':
        print('ninety')
    elif x[0]=='2' and m!='zero':
        print('twenty '+str(m))
    elif x[0]=='3' and m!='zero':
        print('thirty '+str(m))
    elif x[0]=='4' and m!='zero':
        print('forty '+str(m))
    elif x[0]=='5' and m!='zero':
        print('fifty '+str(m))
    elif x[0]=='6' and m!='zero':
        print('sixty '+str(m))
    elif x[0]=='7' and m!='zero':
        print('seventy '+str(m))
    elif x[0]=='8' and m!='zero':
        print('eighty '+str(m))
    elif x[0]=='9' and m!='zero':
        print('ninety '+str(m))


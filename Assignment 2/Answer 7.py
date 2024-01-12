#Assumptions:
# 1) Phone numbers and email ids are not same for different entries

repeatlist=[]
f=open('addrbook.txt')
x=f.read()
if x=="":
    addressbook={}
else:
    addressbook=eval(x)
    for key,value in addressbook.items():
        addressbook[key]=eval(str(value))
f.close()

for key,value in addressbook.items():
    if type(value)==list:
        repeatlist.append(key)

while True:
    print("Press \"1\" to Enter a new entry")
    print("Press \"2\" to Delete an entry")
    print("Press \"3\" to Find an entry by name or partial name")
    print("Press \"4\" to Find an entry by phone number or email")
    print("Press \"5\" to Exit")
    print()

    userinp=input("Enter the number of the option: ")

    if not(userinp=="1" or userinp=="2" or userinp=="3" or userinp=="4" or userinp=="5"):
        print("Please enter a valid input from the listed options")
        print()
    else:
        userinp=int(userinp)
        if userinp==1:
            fault=0
            inpname=input("Enter name: ")
            inpaddr=input("Enter address: ")
            inpphone=input("Enter phone number: ")
            for key,value in addressbook.items():
                if type(value)==list:
                    for element in value:
                        if element['phone']==inpphone:
                            print('Error: this phone number is already associated with an entry')
                            fault = fault + 1
                if type(value)==dict:
                    if value['phone']==inpphone:
                        print('Error: this phone number is already associated with an entry')
                        fault = fault + 1
            if fault==0:
                inpemail=input("Enter email ID: ")
                if type(value)==list:
                    for element in value:
                        if element['email']==inpemail:
                            print('Error: this email address is already associated with an entry')
                            fault=fault + 1
                if type(value)==dict:
                    if value['email']==inpemail:
                        print('Error: this email address is already associated with an entry')
                        fault=fault + 1
                if fault==0:
                    for key,value in addressbook.items():
                        if type(value)==list:
                            for element in value:
                                if element['phone']==inpphone:
                                    print('Error: this phone number is already associated with an entry')
                                    phonefault=phonefault + 1
                    if inpname in addressbook:
                        for key,value in addressbook.items():
                            if key==inpname and type(value)==list:
                                value.append({'address':inpaddr, 'phone':inpphone, 'email':inpemail})
                            if key==inpname and type(value)==dict:
                                addressbook[inpname]=[value]
                                addressbook[inpname].append({'address':inpaddr, 'phone':inpphone, 'email':inpemail})
                    print()
                    print("ENTRY RECORDED, WILL BE ADDED UPON EXITING")
            elif inpname not in addressbook:
                addressbook[inpname]={'address':inpaddr, 'phone':inpphone, 'email':inpemail}
                print()
                print("ENTRY RECORDED, WILL BE ADDED UPON EXITING")
            print()

        if userinp==2:
            count=0
            delentry=input("Enter name of entry to be deleted: ")
            if delentry in addressbook:
                if delentry in repeatlist:
                    print("Multiple entries with this name exist")
                    number=input("Enter phone number of entry you want to delete: ")
                    for key,value in addressbook.items():
                        if key==delentry:
                            if type(value)==list:
                                for element in value:
                                    if element.get('phone')==number:
                                        count=count+1
                                        value.remove(element)
                                        print()
                                        print(f'{delentry}\'s ENTRY RECORDED, WILL BE DELETED UPON EXITING')
                                if len(value)==1:
                                    addressbook[delentry]=value[0]
                                    for i in repeatlist:
                                        if i==delentry:
                                            repeatlist.remove(i)
                    if count==0:
                        print()
                        print("NO ENTRY FOUND WITH GIVEN PHONE NUMBER")
                else:
                    addressbook.pop(delentry)
                    print()
                    print(f'{delentry}\'s ENTRY RECORDED, WILL BE DELETED UPON EXITING')
            else:
                print()
                print("NO ENTRY FOUND AS PER THE GIVEN NAME")
            print()

        if userinp==3:
            count=0
            searchentry=input("Enter the name (full or partial) you want to search: ")
            for name,details in addressbook.items():
                if searchentry.lower() in str(name).lower():
                    count=count+1
                    print(f'{name}: {details}')
            if count==0:
                print()
                print("NO ENTRY FOUND")
            print()

        if userinp==4:
            count=0
            search=input("Enter phone or email associated with entry you want to search: ")
            for key,value in addressbook.items():
                if type(value)==list:
                    for element in value:
                        if element.get('phone')==search or element.get('email')==search:
                            count=count+1
                            print()
                            print(f'{key}: {element}')
                if type(value)==dict:
                    if value.get('phone')==search or value.get('email')==search:
                        count=count+1
                        print()
                        print(f'{key}: {value}')
            if count==0:
                print()
                print("NO ENTRY WITH MATCHING PHONE NUMBER OR EMAIL FOUND")
            print()

        if userinp==5:
            with open('addrbook.txt',mode="w") as f:
                f.write(str(addressbook))
            print("PROGRAM EXIT, ENTRIES UPDATED")
            break


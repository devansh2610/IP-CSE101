gradedict={"A+":10, "A":10, "A-":9, "B":8, "B-":7, "C":6, "C-":5, "D":4, "F":2}
list1=[]

fault=0
sgpa=0
tot_credits=0

while True:
    x=input("Enter details: ")

    if x=="":
        list1.sort()
        for box in list1:
            print(f'{box[0]}: {box[2]}')
        for box in list1:
            for key,value in gradedict.items():
                if box[2]==key:
                    sgpa = sgpa + int(box[1])*value
            tot_credits=tot_credits + int(box[1])
        sgpa=sgpa/tot_credits
        print(f'SGPA: {round(sgpa,2)}')
        break

    else:
        details=x.split()
    
        if len(details)!=3:
            print("Invalid course details")

        else:   
            if not(details[0].isalnum() and details[0].isupper()):
                print("Invalid course name")
                fault=fault+1
            if not((details[1])=="1" or (details[1])=="2" or (details[1])=="4"):
                print("Invalid credits number")
                fault=fault+1
            if not(str(details[2])=="A+" or str(details[2])=="A" or str(details[2])=="A-" or str(details[2])=="B" or str(details[2])=="B-" or str(details[2])=="C" or str(details[2])=="C-" or str(details[2])=="D" or str(details[2])=="F"):
                print("Invalid grade")
                fault=fault+1
            if fault==0:
                list1.append([details[0],int(details[1]),details[2]])
            else:
                fault=0
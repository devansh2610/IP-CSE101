#TAKING INPUT (REGARDLESS OF SORTED OR UNSORTED)
with open('sorted_data.txt') as myfile:
    unsorteddict={}
    for line in myfile:
        line=line.strip('\n')
        if ':' not in line:
            pass
        else:
            name=line[0:(line.find(','))]
            unsorteddict[name] = {'Crossing':[],'Gate':[],'Time':[]} #str(line[(line.find(',') + 2)::])
    myfile.seek(0,0)
    for line in myfile:
        line=line.strip('\n')
        if ':' not in line:
            pass
        else:
            name=line[0:(line.find(','))]
            line=str(line[(line.find(',') + 2)::])
            crossing=line[0:line.find(',')]
            line=str(line[(line.find(',')+2)::])
            gate=line[0:line.find(',')]
            line=str(line[(line.find(',')+2)::])
            time=line[0::]
            unsorteddict[name]['Crossing'].append(crossing)
            unsorteddict[name]['Gate'].append(gate)
            unsorteddict[name]['Time'].append(time)

    #SORTING INPUT
    sortinp=[]
    for key,value in unsorteddict.items():
        for j in range(len(value['Crossing'])):
            sortinp.append((value['Time'][j],key,value['Crossing'][j],value['Gate']))
    sortinp=sorted(sortinp)
    infodict={}
    for key,value in unsorteddict.items():
        infodict[key]= {'Crossing':[],'Gate':None,'Time':[]}
    for j in range(len(sortinp)):
        infodict[sortinp[j][1]]['Crossing'].append(sortinp[j][2])
        infodict[sortinp[j][1]]['Gate'] = sortinp[j][3]
        infodict[sortinp[j][1]]['Time'].append(sortinp[j][0])
    
    #MAIN PROGRAM
    while True:
        print()
        print("Enter 1 to show the record of students moving in/out of campus")
        print("Enter 2 to show the record of students who entered and exited in a given time frame")
        print("Enter 3 to show number of times students have entered/exited the campus through a gate")
        print()
        x=str(input("Enter option: "))
        if x=="":
            break
        if not(x=='1' or x=='2' or x=='3'):
            print("Please enter a valid option")
            print()
        else:
            if x=='1':
                naam=input("Enter name of the student: ")
                samay=input("Enter time to know if student is currently in campus (HH:MM:SS): ")
                list1=[]
                for key,value in infodict.items():
                    if key==naam:
                        for i in range(len(value['Crossing'])):
                            list1.append((value['Gate'][i] , value['Crossing'][i] , value['Time'][i]))
                with open('q2option1.txt',mode="w") as q2option1:
                    q2option1.write(str(list1))
                for key,value in infodict.items():
                    if key==naam:
                        if samay in value['Time']:
                            for i in range(len(value['Time'])):
                                if value['Time'][i]==samay:
                                    if value['Crossing'][i]=='EXIT': print(f'Student still in campus: NO')
                                    if value['Crossing'][i]=='ENTER': print(f'Student still in campus: YES')
                                    print()
                        else:
                            if samay>value['Time'][-1]:
                                if value['Crossing'][-1]=='EXIT': print(f'Student still in campus: NO')
                                if value['Crossing'][-1]=='ENTER': print(f'Student still in campus: YES')
                                print()
                            elif samay<value['Time'][0]:
                                if value['Crossing'][0]=='EXIT': print(f'Student still in campus: YES')
                                if value['Crossing'][0]=='ENTER': print(f'Student still in campus: NO')
                                print()
                            else:
                                i=0
                                while True:
                                    if samay>value['Time'][i]:
                                        i=i+1
                                    if samay<value['Time'][i]:
                                        i=i-1
                                        if value['Crossing'][i]=='EXIT': print(f'Student still in campus: NO')
                                        if value['Crossing'][i]=='ENTER': print(f'Student still in campus: YES')
                                        print()
                                        break

        if x=='2':
            start_time=str(input("Enter start time (HH:MM:SS): "))
            end_time= str(input("Enter end time (HH:MM:SS): "))
            opt2list=[]
            for key,value in infodict.items():
                for j in range(len(value['Time'])):
                    if value['Time'][j]>=start_time and value['Time'][j]<=end_time:
                        opt2list.append((value['Time'][j],key,value['Crossing'][j],value['Gate'][j]))
            opt2list=sorted(opt2list)
            with open('q2option2.txt',mode="w") as q2option2:
                for j in range(len(opt2list)):
                    q2option2.write(str(f'{opt2list[j][1]}, {opt2list[j][2]}, {opt2list[j][3]}, {opt2list[j][0]}\n'))

        if x=='3':
            gateinp=str(input("Enter gate number: "))
            entry=0
            exit=0
            for key,value in infodict.items():
                for j in range(len(value['Gate'])):
                    if value['Gate'][j]==gateinp:
                        if value['Crossing'][j]=='ENTER':
                            entry=entry+1
                        if value['Crossing'][j]=='EXIT':
                            exit=exit+1
            print(f'Number of entries: {entry}')
            print(f'Number of exits: {exit}')







import time

def add_course(cname, credits, assessments, policy):
    details = {}
    details['name'] = cname
    details['credits'] = credits
    details['assessments'] = assessments
    details['policy'] = policy
    return details

IP = add_course('IP', 4,  [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)], [80, 65, 50, 40])

def get_marks(course=IP, file='marks.txt'):
    studentinfo={}
    with open(file) as myfile:
        for line in myfile:
            line=line.strip('\n').split()
            roll_no = line[0]
            marks = [float(elt) for elt in line[1::]]
            tot_marks= 0
            for elt in marks: tot_marks = tot_marks + elt
            studentinfo[roll_no] = (tot_marks,marks)
    return studentinfo

def cutoff(f=get_marks,course=IP,file='marks.txt'):
    studentinfo = get_marks(course,file)
    Alist=sorted([value[0] for value in studentinfo.values() if value[0]>=80 and value[0]<=100],reverse=True)
    Blist=sorted([value[0] for value in studentinfo.values() if value[0]>=65 and value[0]<80],reverse=True)
    Clist=sorted([value[0] for value in studentinfo.values() if value[0]>=50 and value[0]<65],reverse=True)
    Dlist=sorted([value[0] for value in studentinfo.values() if value[0]>=40 and value[0]<=50],reverse=True)
    Flist=sorted([value[0] for value in studentinfo.values() if value[0]<40],reverse=True)
    diffA=[Alist[i] - Alist[i+1] for i in range(len(Alist)) if (i+1)<=(len(Alist)-1)]
    diffB=[Blist[i] - Blist[i+1] for i in range(len(Blist)) if (i+1)<=(len(Blist)-1)]
    diffC=[Clist[i] - Clist[i+1] for i in range(len(Clist)) if (i+1)<=(len(Clist)-1)]
    diffD=[Dlist[i] - Dlist[i+1] for i in range(len(Dlist)) if (i+1)<=(len(Dlist)-1)]
    diffF=[Flist[i] - Flist[i+1] for i in range(len(Flist)) if (i+1)<=(len(Flist)-1)]
    if len(diffA)>0:
        indexA = diffA.index(max(diffA))
        cutoffA = (Alist[indexA] + Alist[indexA + 1]) / 2
        if cutoffA > IP['policy'][0] + 2: cutoffA = IP['policy'][0] + 2
        if cutoffA < IP['policy'][0] - 2: cutoffA = IP['policy'][0] - 2
    else:
        cutoffA = IP['policy'][0]
    if len(diffB)>0:
        indexB = diffB.index(max(diffB))
        cutoffB = (Blist[indexB] + Blist[indexB + 1]) / 2
        if cutoffB > IP['policy'][1] + 2: cutoffB = IP['policy'][1] + 2
        if cutoffB < IP['policy'][1] - 2: cutoffB = IP['policy'][1] - 2
    else:
        cutoffB = IP['policy'][1]
    if len(diffC)>0:
        indexC = diffC.index(max(diffC))
        cutoffC = (Clist[indexC] + Clist[indexC + 1]) / 2
        if cutoffC > IP['policy'][2] + 2: cutoffC = IP['policy'][2] + 2
        if cutoffC < IP['policy'][2] - 2: cutoffC = IP['policy'][2] - 2
    else:
        cutoffC = IP['policy'][2]
    if len(diffD)>0:
        indexD = diffD.index(max(diffD))
        cutoffD = (Dlist[indexD] + Dlist[indexD + 1]) / 2
        if cutoffD > IP['policy'][3] + 2: cutoffD = IP['policy'][3] + 2
        if cutoffD < IP['policy'][3] - 2: cutoffD = IP['policy'][3] - 2
    else:
        cutoffD = IP['policy'][3]
    return [cutoffA,cutoffB,cutoffC,cutoffD]

def gradebycutoff(x,f1=cutoff):
    cutofflist=cutoff()
    if float(x)>=cutofflist[0]: return 'A'
    if float(x)<cutofflist[0] and float(x)>=cutofflist[1]: return 'B'
    if float(x)<cutofflist[1] and float(x)>=cutofflist[2]: return 'C' 
    if float(x)<cutofflist[2] and float(x)>=cutofflist[3]: return 'D'
    if float(x)<cutofflist[3]: return 'F'

def do_grading(f1=get_marks,f2=gradebycutoff):
    studentinfo = get_marks()
    students=[]
    for key,value in studentinfo.items():
        students.append((key,value[0],gradebycutoff(value[0])))
    return students

'''start = time.time()
for k in range(1000):
    do_grading()
end=time.time()
print(f'Time taken by grading func {end - start}')'''

while True:
    print()
    print("1. Generate a summary")
    print("2. Print the grades of all the students in a file")
    print("3. Search for a student record")
    print()
    x=str(input())
    if x=="":
        break
    else:
        if x=="1":
            print(f'Course name: {IP["name"]}')
            print(f'Credits: {IP["credits"]}')
            print(f'Assessments: {IP["assessments"]}')
            print(f'Original Grading Policy: {IP["policy"]}')
            print(f'Revised Grading Policy: {cutoff()}')
            print()
            students = do_grading()
            Agraders=0
            Bgraders=0
            Cgraders=0
            Dgraders=0
            Fgraders=0
            for elt in students:
                if elt[2]=='A': Agraders = Agraders + 1
                if elt[2]=='B': Bgraders = Bgraders + 1
                if elt[2]=='C': Cgraders = Cgraders + 1
                if elt[2]=='D': Dgraders = Dgraders + 1
                if elt[2]=='F': Fgraders = Fgraders + 1
            print(f'Students with A grade: {Agraders}')
            print(f'Students with B grade: {Bgraders}')
            print(f'Students with C grade: {Cgraders}')
            print(f'Students with D grade: {Dgraders}')
            print(f'Students with F grade: {Fgraders}')

        if x=='2':
            students = do_grading()
            with open('outputq5.txt',mode="a") as output:
                for elt in students:
                    output.write(f'{elt[0]}, {elt[1]}, {elt[2]}\n')
            print('Grades have been printed in the file')

        if x=='3':
            #startsearch=time.time()
            #for i in range(50):
                #inprollno='2022001'
            infodict=get_marks()
            newdict={}
            for key,value in infodict.items():
                newdict[key]=[[]]

            for key,value in newdict.items():
                for j in range(len(IP['assessments'])):
                    newdict[key][0].append([IP['assessments'][j][0],None])
            
            for key,value in infodict.items():
                for k,v in newdict.items():
                    if key==k:
                        v.append(value[0])
                        for j in range(len(value[1])):
                            v[0][j][1] = value[1][j]
                        v.append(gradebycutoff(value[0]))

            inprollno=str(input("Enter roll number: "))
            for key,value in newdict.items():
                if key==inprollno:
                    print(f'Assessments:',end=" ")
                    for j in range(len(value[0])):
                        if value[0][j]!=value[0][-1]: print(value[0][j],end=", ")
                        if value[0][j]==value[0][-1]: print(value[0][j])
                    print(f'Total Marks: {value[1]}')
                    print(f'Grade: {value[2]}')
            #endsearch=time.time()
            #print(f'Time taken for search func is {endsearch - startsearch}')

                        



        





import time

class Course():
    def __init__(self,name,credits,assessments,policy):
        self.name = name
        self.credits = credits
        self.assessments = assessments
        self.policy = policy

    def course_details(self):    
        details = {}
        details['name'] = self.name
        details['credits'] = self.credits
        details['assessments'] = self.assessments
        details['policy'] = self.policy
        return details        

    def upload_marks(self,file='marks.txt'):
        studentinfo={}
        with open(file) as myfile:
            for line in myfile:
                line=line.strip('\n').split()
                roll_no=line[0]
                marks = [float(elt) for elt in line[1::]]
                tot_marks= 0
                for elt in marks: tot_marks = tot_marks + elt
                studentinfo[roll_no] = (tot_marks,marks)
        return studentinfo

    def cutoff(self):
        Alist = sorted([value[0] for value in Course.upload_marks(self).values() if value[0]>=80 and value[0]<=100],reverse=True)
        Blist = sorted([value[0] for value in Course.upload_marks(self).values() if value[0]>=65 and value[0]<80],reverse=True)
        Clist = sorted([value[0] for value in Course.upload_marks(self).values() if value[0]>=50 and value[0]<65],reverse=True)
        Dlist = sorted([value[0] for value in Course.upload_marks(self).values() if value[0]>=40 and value[0]<=50],reverse=True)
        diffA = [Alist[i] - Alist[i+1] for i in range(len(Alist)) if (i)<(len(Alist)-1)]
        diffB = [Blist[i] - Blist[i+1] for i in range(len(Blist)) if (i)<(len(Blist)-1)]
        diffC = [Clist[i] - Clist[i+1] for i in range(len(Clist)) if (i)<(len(Clist)-1)]
        diffD = [Dlist[i] - Dlist[i+1] for i in range(len(Dlist)) if (i)<(len(Dlist)-1)]

        if len(diffA)>0: 
            indexA = diffA.index(max(diffA))
            cutoffA = ((Alist[indexA] + Alist[indexA + 1]) / 2)
            if cutoffA > Course.course_details(self)['policy'][0] + 2: cutoffA = Course.course_details(self)['policy'][0] + 2
            if cutoffA < Course.course_details(self)['policy'][0] - 2: cutoffA = Course.course_details(self)['policy'][0] - 2
        else:
            cutoffA = Course.course_details(self)['policy'][0]
        
        if len(diffB)>0:
            indexB = diffB.index(max(diffB)) 
            cutoffB = ((Blist[indexB] + Blist[indexB + 1]) / 2)
            if cutoffB > Course.course_details(self)['policy'][1] + 2: cutoffB = Course.course_details(self)['policy'][1] + 2
            if cutoffB < Course.course_details(self)['policy'][1] - 2: cutoffB = Course.course_details(self)['policy'][1] - 2
        else:
            cutoffB = Course.course_details(self)['policy'][1]
        
        if len(diffC)>0:
            indexC = diffC.index(max(diffC))
            #if len(diffC)==1: cutoffC = ((Clist[indexC]))
            cutoffC = ((Clist[indexC] + Clist[indexC + 1]) / 2)
            if cutoffC > Course.course_details(self)['policy'][2] + 2: cutoffC = Course.course_details(self)['policy'][2] + 2
            if cutoffC < Course.course_details(self)['policy'][2] - 2: cutoffC = Course.course_details(self)['policy'][2] - 2
        else:
            cutoffC = Course.course_details(self)['policy'][2]

        if len(diffD)>0:
            indexD = diffD.index(max(diffD))
            cutoffD = ((Dlist[indexD] + Dlist[indexD + 1]) / 2)
            if cutoffD > Course.course_details(self)['policy'][3] + 2: cutoffD = Course.course_details(self)['policy'][3] + 2
            if cutoffD < Course.course_details(self)['policy'][3] - 2: cutoffD = Course.course_details(self)['policy'][3] - 2
        else:
            cutoffD = Course.course_details(self)['policy'][3]

        return [cutoffA,cutoffB,cutoffC,cutoffD]

IP = Course('IP',4,[("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)],[80, 65, 50, 40, 30])

class Student():
    def __init__(self,course=IP,cutoff=IP.cutoff()):
        self.course = course
        self.cutoff = course.cutoff()
    
    def gradebycutoff(self,x,course=IP):
        if float(x)>=IP.cutoff()[0]: return 'A'
        if float(x)<IP.cutoff()[0] and float(x)>=IP.cutoff()[1]: return 'B'
        if float(x)<IP.cutoff()[1] and float(x)>=IP.cutoff()[2]: return 'C' 
        if float(x)<IP.cutoff()[2] and float(x)>=IP.cutoff()[3]: return 'D'
        if float(x)<IP.cutoff()[3]: return 'F'
    
    def do_grading(self,course=IP):
        studentinfo = course.upload_marks()
        students=[]
        for key,value in studentinfo.items():
            students.append((key,value[0],Student.gradebycutoff(self,value[0])))
        return students

'''start=time.time()
for k in range(1000):
    Student.do_grading(IP)
end=time.time()
print(f'Time taken by grading function is {end - start}')'''

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
            print(f'Course name: {IP.course_details()["name"]}')
            print(f'Credits: {IP.course_details()["credits"]}')
            print(f'Assessments: {IP.course_details()["assessments"]}')
            print(f'Original Grading Policy: {IP.course_details()["policy"]}')
            print(f'Revised Grading Policy: {IP.cutoff()}')
            print()
            students = Student.do_grading(IP)
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
            students = Student.do_grading(IP)
            with open('outputq4.txt',mode="a") as output:
                for elt in students:
                    output.write(f'{elt[0]}, {elt[1]}, {elt[2]}\n')
            print('Grades have been printed in the file')


        if x=='3':
            #startsearch=time.time()
            #for k in range(50):
                #inprollno='2022001'
            details = IP.course_details()
            studentinfo = IP.upload_marks()
            students = Student.do_grading(IP)
            inprollno=str(input("Enter roll number: "))
            print('Assessments:',end=" ")
            for key,value in studentinfo.items():
                if key==inprollno:
                    for i in range(len(value[1])):
                        if value[1][i]!=value[1][-1]:
                            print([details['assessments'][i][0], value[1][i]], end =", ")
                        if value[1][i]==value[1][-1]:
                            print([details['assessments'][i][0], value[1][i]])
                    for i in range(len(students)):
                        if students[i][0]==inprollno:
                            print(f'Total Marks: {students[i][1]}')
                            print(f'Grade: {students[i][2]}')
            #endsearch=time.time()
            #print(f'Time taken by search func is {endsearch - startsearch}')
                
                    
                

            
    



    


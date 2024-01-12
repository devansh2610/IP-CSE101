#Assumptions:
# Data in IPmarks.txt is written exactly in the format as in Assignment doc.

with open ('IPmarks.txt') as marksfile:
        with open ('IPgrades.txt',mode="a") as gradefile: 
            wts = wts= [(10, 5), (20, 5), (100, 15), (40, 10),(80, 40),(50, 25)]
            for line in marksfile:
                weightedavg=0
                totalmarks=0
                list1=line.split(", ")
                for i in range(len(list1)):
                    if i==0:
                        rollno=list1[0]
                    if i!=0:
                        totalmarks = totalmarks + int(list1[i])
                        weightedavg = weightedavg + int(list1[i])*((wts[i-1][1])/(wts[i-1][0]))
                if weightedavg>=80:
                    grade="A"
                elif weightedavg>=70 and weightedavg<80:
                    grade="A-"
                elif weightedavg>=60 and weightedavg<70:
                    grade="B"
                elif weightedavg>=50 and weightedavg<60:
                    grade="B-"
                elif weightedavg>=40 and weightedavg<50:
                    grade="C"
                elif weightedavg>=35 and weightedavg<40:
                    grade="C-"
                elif weightedavg>=30 and weightedavg<35:
                    grade="D"
                elif weightedavg<30:
                    grade="F"

                gradefile.write(rollno)
                gradefile.write(", ")
                gradefile.write(str(totalmarks))
                gradefile.write(", ")
                gradefile.write(grade)
                gradefile.write('\n')
            print("Entries have been recorded in IPgrades.txt")


                
                


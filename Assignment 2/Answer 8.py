#Assumptions:
# 1) If URL0x in references of URL0x, then this case will not be considered for calculation.
# 2) If URL0y is present in references of URL0x more than once, then it is counted only once as a unique reference.
# 3) Data in pages.txt is exactly in the form as written in the Assignment doc.

with open ('C:\\Users\\Devansh\\Documents\\IP Python Assignments\\Assignment 2\\Assignment 2 base\\answer 8\\testcase 4.txt') as myfile:
    uniquedict={}
    initial_imp_dict={}
    urllist=[]
    
    for line in myfile:
        comma_index=line.find(",")
        urlstr=line[0:comma_index]
        urllist.append(urlstr)
        colon_index=line.find(":")
        initimp=float(line[(comma_index+1):(colon_index)])
        initial_imp_dict[urlstr]=initimp
    
    for key in initial_imp_dict.keys():
        uniquedict[key]=[]

    myfile.seek(0)
    for line in myfile:
        for key in initial_imp_dict.keys():
            comma_index=line.find(",")
            if line[0:comma_index]==key:
                for element in urllist:
                    if element in line[comma_index::]:
                        uniquedict[key].append(element)

    overall_imp_dict={}
    for k,v in initial_imp_dict.items():
        overall_imp_dict[k]=0

    for key in uniquedict.keys():
        for k,v in uniquedict.items():
            if key in v:
                if key==k:
                    pass
                else:
                    if len(uniquedict[k])>0:
                        overall_imp_dict[key]= overall_imp_dict[key] + initial_imp_dict[k]/(len(uniquedict[k]))
                    else:
                        overall_imp_dict[key] = -777

    orderlist=[]
    for key,value in overall_imp_dict.items():
        orderlist.append([value,key])
    orderlist.sort(reverse=True)
    for element in orderlist:
        if element[0]==-777:
            element[0]="Divison not possible because denominator = 0"

    N=int(input("Enter N: "))
    if N>len(urllist):
        print(f"Enter a smaller number (N<={len(urllist)})")
    else:
        for i in range(N):
            print(f'{orderlist[i][1]}: {orderlist[i][0]}')
    









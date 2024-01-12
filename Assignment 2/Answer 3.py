#Assumptions:
# 1) Data in yearbook.txt is written exactly in the format as written in the Assignment doc.

with open('yearbook.txt') as myfile:
    yearbook={}
    keylist=[]
    for line in myfile:
        line=line.replace('\n',"")
        if ":" in line:
            keylist.append(line)

    myfile.seek(0,0)
    for line in myfile:
        line=line.replace('\n',"")
        if line in keylist:
            value={}
            key=line.replace(":","")
            yearbook[key]=value
        if line not in keylist:
            if line!="":
                if ", " in line:
                    valuelist = line.split(", ")
                    value[valuelist[0]]=int(valuelist[1])
                    yearbook[key]=value
                if "," in line:
                    valuelist = line.split(",")
                    value[valuelist[0]]=int(valuelist[1])
                    yearbook[key]=value
                    
    namesign={}
    for key,value in yearbook.items():
        total=0
        for k,v in value.items():
            total= total + v
            namesign[key]=total

    signcount=[]
    for key,value in namesign.items():
        signcount.append(value)

    print("Max: ")
    for i in namesign.keys():
        if namesign[i]==max(signcount):
            print(i,end=", ")
    print(f'signatures = {min(signcount)}')
    print()
    print("Min: ")
    for i in namesign.keys():
        if namesign[i]==min(signcount):
            print(i,end=", ")
    print(f'signatures = {min(signcount)}')





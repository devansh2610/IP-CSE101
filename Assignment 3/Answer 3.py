#ASSUMPTIONS:
# 1) EACH NEW LINE IN THE INPUT FILE IS CONSIDERED AS A NEW SENTENCE REGARDLESS OF IF THE PREV LINE ENDS WITH A FULL STOP 
# 2) A SINGLE/STANDALONE FULLSTOP ('.') IS ALSO CONSIDERED AS THE END OF A LINE 

inplist=['file1.txt','file2.txt','file3.txt','file4.txt','file5.txt']
for elt in inplist:
    name=elt
    with open(elt) as myfile:

        text=[] #text by each line in file (not sentence)
        words=[] #list with only words - no other characters
        for line in myfile:
            line = line.strip('/n').lower()
            text.append(line.split())
        for i in range(len(text)):
            for j in range(len(text[i])):
                words.append(text[i][j])

        for i in range(len(words)):
            words[i] = words[i].replace(",","")
            words[i] = words[i].replace(".","")
            words[i] = words[i].replace(";","")
            words[i] = words[i].replace(":","")
            words[i] = words[i].replace("-","")

        for x in range(20):        
            for elt in words:
                if elt=='' or elt ==' ' or elt=='   ':
                    words.remove(elt)
        
        tempsentence=[] #temp list containing each sentence
        myfile.seek(0,0)
        for line in myfile:
            line=line.strip('\n').lower()
            i=0
            while True:
                if (i+1)>(len(line)-1):
                    tempsentence.append(line[0:i])
                    line=line[(i)::]
                    break
                if line[i]==".":
                    if not(line[i-1]=="." or line[i-1]=="," or line[i-1]==":" or line[i-1]==";" or line[i-1]=="-") and not(line[i+1]=="." or line[i+1]=="," or line[i+1]==":" or line[i+1]==";" or line[i+1]=="-"):
                        tempsentence.append(line[0:i])
                        line=line[(i+1)::]
                        i=0
                i=i+1
                    
        sentences=[] #main list for sentences
        for i in range(len(tempsentence)):
            sentences.append([tempsentence[i]])
        for i in range(len(sentences)):
            sentences[i][0] = sentences[i][0].strip(' ')
        for j in range(20):
            for elt in sentences:
                if elt==[''] or elt ==[' '] or elt==[]:
                    sentences.remove(elt)

        def factor1(list1=words):
            uniquewords=set()
            for elt in list1:
                uniquewords.add(elt)
            if len(list1)>0: f1 = len(uniquewords)/len(list1)
            else: f1=0
            return f1

        def factor2(list1=words):
            totwords=len(list1) # total words
            # creating tempdict to store elt:freq and then creating sorted list of elts by freq
            tempdict={}
            for elt in list1: 
                tempdict[elt] = list1.count(elt)
            totoccur_list = sorted(tempdict, key=lambda x: tempdict[x], reverse=True) #sorted list
            totoccur_dict={}
            for elt in totoccur_list:
                totoccur_dict[elt] = tempdict[elt]   #new dict to create elt:freq in sorted by keys manner
            from collections import Counter
            top5 = Counter(totoccur_dict).most_common(5)
            numerator = 0 
            for i in range(len(top5)):
                numerator = numerator + top5[i][1]
            if len(list1)>0: f2 = numerator/len(list1)
            else: f2=0
            return f2

        def factor3(list1=sentences):
            splitwords=[]
            for i in range(len(list1)):
                for j in range(len(list1[i])):
                    splitwords.append(str(list1[i][j]).replace('-','').replace(',','').replace(':','').replace('.','').replace(';','').split())
            grt35=0
            less5=0
            for i in range(len(splitwords)):
                if len(splitwords[i])>35: grt35 = grt35 + 1
                if len(splitwords[i])<5: less5 = less5 + 1
            if len(list1)>0: f3 = (grt35 + less5)/len(list1)
            else: f3=0
            return f3

        def factor4(list1=sentences,list2=words):
            count = 0
            number = 1
            for i in range(len(list1)):
                j=0
                while True:
                    if (j+1)>((len(str(list1[i][0]))-1)):
                        break
                    if list1[i][0][j]=="." or list1[i][0][j]=="," or list1[i][0][j]==":" or list1[i][0][j]==";" or list1[i][0][j]=="-":
                        if not(list1[i][0][j+1]=="." or list1[i][0][j+1]=="," or list1[i][0][j+1]==":" or list1[i][0][j+1]==";" or list1[i][0][j+1]=="-"):
                            if list1[i][0][j-1]=="." or list1[i][0][j-1]=="," or list1[i][0][j-1]==":" or list1[i][0][j-1]==";" or list1[i][0][j-1]=="-":
                                count=count + 1
                        if list1[i][0][j+1]=="." or list1[i][0][j+1]=="," or list1[i][0][j+1]==":" or list1[i][0][j+1]==";" or list1[i][0][j+1]=="-":
                            number = number+1
                    j=j+1
            f4 = count/(len(list2))
            return f4

        def factor5(list1=words):
            if len(list1)>750: f5=1
            else: f5 = 0
            return f5
                
        netscore= 4 + (factor1())*6 + (factor2())*6 -(factor3()) - (factor4()) - (factor5())
        from collections import Counter
        top5words = Counter(words).most_common(5)
        import random
        random5words = [words[random.randint(0,(len(words)-1))] for x in range(5)]

    with open('scores.txt',mode="a") as output:
        output.write(f'1. {name}\n')
        output.write(f'2. score: {netscore}\n')
        output.write(f'3. Top 5 words: {top5words}\n')
        output.write(f'4. Random 5 words: {random5words}\n')
        output.write('\n')

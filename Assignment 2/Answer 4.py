#Assumptions:
# 1) If number of letters in user's input is not 5 then that will not be counted as a try.
# 2) If a letter appears more than twice in the word and the user guesses the letter (at incorrect place) then it will only be shown in 
# other characters present once. However, if the user guesses its place correctly at least once then it will still be shown in other characters 
# present to indicate that it appears more than once.
# 3) User can input the word in both lowercase as well as uppercase or both - for simplicity.
 
list1=["Abuse","Adult",'Agent','Anger','Apple','Award','Basis','Beach','Birth','Blood','Board','Brain','Bread','Break','Brown','Buyer','Cause','Chain','Chair','Chest','Chief','Child','China','Claim','Class','Clock','Coach','Coast','Court','Cover','Cream','Crime','Cross','Crowd','Crown','Cycle','Dance','Death','Depth','Index','Input','Issue','Japan','Jones','Judge','Knife','Laura','Pilot','Phone','Peter']
import random
word=list1[random.randint(0,len(list1))]

otherchar=[]

tries=0

while True:
    userinp=str(input("enter guess: "))
    if len(userinp)!=5:
        print("Invalid input: Your input contains more than 5 letters.")
        if tries>0:
            tries=tries-1

    else:
        userinp=userinp.lower()
        word=word.lower()
        #for printing chars which are in correct places
        for i in range(len(userinp)):
            if userinp[i]==word[i]:
                print(word[i],end="")
            else:
                print("-",end="")
        print()

        #for printing other characters present guessed at incorrect places
        for i in range(len(userinp)):
            if not(userinp[i]==word[i]) and userinp[i] in word: #and userinp[i] not in userinp[0:i]:
                otherchar.append(userinp[i])
        if len(otherchar)==0 and userinp!=word:
            print("other characters present: None, other characters guessed incorrectly")                
        if len(otherchar)>0:
            print("other characters present: ",end="")
            for elt in otherchar:
                if elt==otherchar[-1]:
                    print(elt)
                else:
                    print(elt,end=",")
            otherchar=[]

    if userinp==word:
        print(f"Correct guess! {word.capitalize()} is the correct word.")
        break
    else:
        tries=tries+1
        if tries==6:
            print("Max tries reached")
            print(f"The correct word is {word.capitalize()}")
            break    
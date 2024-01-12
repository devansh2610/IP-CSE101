list1=[]

while True:
    coord=input("enter coordinates as x,y: ")
    if coord=="":
        print()
        break
    else:
        coord=coord.split(",")
        list1.append((coord[0],coord[1]))
        coord=[]

m1=[[int(elt[0]),int(elt[1]),1] for elt in list1]

cx=int(input("enter cx: "))
cy=int(input("enter cy: "))

m2=[[cx,0,0], [0,cy,0], [0,0,1]]

#len(m2[0]) represents columns of resulting matrix, len(m1) represents rows of resulting matrix
matrix=[[0 for i in range(len(m2[0]))] for j in range(len(m1))]

for i in range(len(m1)):
    for j in range(len(m1[i])):
        for box in m2:
            matrix[i][j] = matrix[i][j] + (m1[i][j])*(box[j])


list2=[(elt[0],elt[1]) for elt in matrix]
print(f'list of coordinates is: {list2}')





x0=float(input("Enter current x-coordinate:"))
y0=float(input("Enter current y-coordinate:"))
distn=0
dists=0
distw=0
diste=0
totdist=0

while True:
    inputdist=float(input("Enter distance to be travelled:"))
    if inputdist<=0:
        break
    else:
        totdist=totdist+inputdist
        if inputdist<=25 and inputdist>0:
            distn=distn+inputdist
        elif inputdist>=26 and inputdist<=50:
            dists=dists+inputdist
        elif inputdist>=51 and inputdist<=75:
            diste=diste+inputdist
        elif inputdist>=76:
            distw=distw+inputdist

x1=diste-distw+x0
y1=distn-dists+y0
distofcoord=(((x1-x0)**2)+((y1-y0)**2))**0.5

print(f'Final coordinate of the vehicle is: {(x1,y1)}')
print(f'Total distance travelled is: {totdist} units')
print(f'Straight line distance between initial and final locations is: {distofcoord}')



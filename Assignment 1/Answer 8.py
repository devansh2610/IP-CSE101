pop = [50,1450,1400,1700,1500,600,1200]
currentpop = sum(pop)

print(f"Current population is {currentpop}")
rate=2.5
growthrate=[rate - (index*0.4) for index in range(len(pop))]

oldpop=currentpop
newpop=currentpop
Y=1

while True:
    for i in range(len(growthrate)):
        pop[i] = pop[i] + (pop[i]*(growthrate[i]/100))
        growthrate[i] = growthrate[i] - 0.1
    oldpop=newpop
    newpop=sum(pop)
    if newpop<oldpop:
        print(f'Maximum population is: {oldpop}')
        print(f'Number of years is: {Y}')
        break
    Y=Y+1  

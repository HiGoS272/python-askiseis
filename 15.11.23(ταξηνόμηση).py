lo=[]
ly=[]

sum = 0
c = 0

o= raw_input("Dwse onoma:")

while o!="T":
    y= input("dwse ypsos:")      
    sum = sum + y
    if y > 140 and y<=150:
        c = c + 1
    lo.append(o)
    ly.append(y)
    o= raw_input("Dwse onoma:")

for i in range(len(ly)-1)
    for j in range(len(ly)-1, i , -1)
        if ly[j-1] < ly[j]
        ly[j-1],ly[j] = ly[j] , ly[j-1]
        lo[j-1],lo[j] = lo[j] , lo[j-1]
            
    

    
megethos = len(ly)
if megethos > 0:
    mo = sum/ megethos
print "O Mesos oros einai:",mo
print "Oi mathites pou exoun ypsos apo 1.40 ews 150 einai:",c
        

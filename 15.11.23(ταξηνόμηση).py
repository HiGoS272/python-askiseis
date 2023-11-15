#ΕΚΦΩΝΗΣΗ ΑΣΚΗΣΗΣ:
# Να καταχωρήσετε τα ονόματα και το ύψος (cm) των μαθητών μιας τάξης.
#Σταματάει η είσοδος των δεδομένων όταν δοθεί αντί για όνομα το γράμμα “Τ”.
#Να υπολογίσετε τον ΜΟ του ύψους της τάξης.
#Να εμφανίσετε πόσοι μαθητές έχουν ύψος από 140 έως 150 cm.
#Να εμφανίσετε τα ονόματα των 5 ψηλότερων.

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
        

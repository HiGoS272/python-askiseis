#ΣΥΝΑΡΤΗΣΗ

def TYROS_EMB(age):
    if age >=40 and age<=50:
        return 1
    elif age>=51 and age <=60:
        return 2
    elif age >=61 and age <=70:
        return 3
    else:
        return 4
 
ILIKIA = []
AMKA = []
FILO = []
#COUNTER ΓΙΑ ΤΙΣ ΓΥΝΑΙΚΕΣ
c = 0
#COUNTER ΓΙΑ ΤΟ ΠΟΣΟΙ ΕΙΝΑΙ ΟΛΟΙ
c1 = 0

age = int(input("Give The Age:"))

while age > 40:
 
    age = int(input("Give The Age:"))
    sex = raw_input("Give The Sex of people, Α OR Γ:")
    
    while sex!="A" and sex!="G":
        sex = raw_input("Give The Sex of people, Α OR Γ:")

    if sex=="G":
        c = c+1
        
    amka = raw_input("Give The A.M.K.A.:")
    
    AMKA.append(amka)
    ILIKIA.append(age)
    FILO.append(sex)

    x =TYROS_EMB(age)
    print x , amka
    
    age = int(input("Give The Age:"))
    
    c1 = c1 + 1
        


max_val2 = 0
idx_max2 = 0

for i in range(len(ILIKIA)):
    if ILIKIA[i] > max_val:
        max_val2=ILIKIA[i]
        idx_max2 = i
print ILIKIA[idx_max2], AMKA[idx_max2],FILO[idx_max2]

#ΠΟΣΟΣΤΟ ΤΩΝ ΓΥΝΑΙΚΩΝ
pososto = (c / c1) * 100
print pososto





    

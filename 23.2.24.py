OMADES = []
BATHMOI = []
PROK = []
BATHPROK = []


for i in range(100):
    team = raw_input("Give The Team Of Dance:")
    ratings = int(input("Give The Ratings:"))

    OMADES.append(team)
    BATHMOI.append(ratings)

for i in range(len(BATHMOI)):
    if BATHMOI[i]>150:
        PROK.append(OMADES[i])
        BATHPROK.append(BATHMOI[i])

x = len(BATHPROK)
for i in range(x-1):
    for j in range(x-i-1):
    if j BATHPROK[j]>BATHPROK[j-1]
      BATHPROK[j],BATHPROK[j-1] = BATHPROK[j-1],BATHPROK[j]
      
print BATHPROK      

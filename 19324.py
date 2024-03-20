ON = []
NIKES = []
HTTES = []
SYN = []

team = raw_input("Give The Name Of  Basketball Team:")

while team !="TELOS":

    team = raw_input("Give The Name Of  Basketball Team:")
    win = int(input("Give The Wins of Teams:")
    lose = int(input("Give The lose of Teams:")


    NIKES.append(win)
    HTTES.append(lose)
    ON.append(team)
               
    score=win*2+lose
    print grade
    SYN.append(score)


               
    for i in range(len(SYN)-1):  
        for j in range(len(SYN)-1,i,-1):  
            if(SYN[j-1]<SYN[j]):
               ON[j],ON[j-1]=ON[j-1],ON[j]
               NIKES[j],NIKES[j-1]=NIKES[j-1],NIKES[j]
               HTTES[j],HTTES[j-1]=HTTES[j-1],HTTES[j]
               SYN[j],SYN[j-1]=SYN[j-1],SYN[j]



    for i in range(len(ON)):
        print ON[i]
        print NIKES[i]
        print HTTES[i]
        print SYN[i]


    for i in range(len(HTTES)):
        HTTES[i]<4:
            print ON[i]
               
            
    
               
    team = raw_input("Give The Name Of  Basketball Team:")
x = open("apotelesmata.txt","w")
for i in range (len(ON)):
               x.write(ON[i])
               x.write(str(NIKES[i]))
               x.write(str(ETTES[i]))
               x.write(str(SYN[i]))
    
    

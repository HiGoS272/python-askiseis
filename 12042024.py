#askisi me MENU

ans=1

while ans!="7":
    print "1.Πρόσθεση"
    print "2.Αφαίρεση"
    print "3. Πολλαπλασιασμός"
    print "4. Διαίρεση"
    print "5. Ακέραιο υπόλοιπο"
    print "6. Δυνάμεις"
    print "7. Έξοδος"
    
    ans=raw_input("What would you like to do?")
    if ans!="7":
        ar1 = int(input("dwse arithmo1:"))
        ar2 = int(input("dwse arithmo2:"))
    
    #1
    if ans=="1":
        print "\n Πρόσθεση Added"
        x = ar1+ar2
        print x
    #2    
    elif ans=="2":
        print "\n .Αφαίρεση"
        y =  ar1-ar2
        print y
    #3    
    elif ans=="3":
        print "\n Πολλαπλασιασμός"       
        z =   ar1*ar2
        print z
    #4    
    elif ans=="4":
        print "\n Διαίρεση"
        if ar2>0:
            o = ar1/ar2
            print o
    #5            
    elif ans=="5":
        print "\n Ακέραιο υπόλοιπο"
        if ar2>0:
            p = ar1%ar2
            print p
    #6        
    elif ans=="6":
        print "\n Δυνάμεις"
        k =   ar1**ar2
        print k
    #7    
    if ans =="7":
        print "TELOS"

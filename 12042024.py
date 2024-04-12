#askisi me MENU

ans=1

while ans!="7":
    print "1.prosthesi"
    print "2.aferesi"
    print "3. pollaplasiasmos"
    print "4. dieresi"
    print "5. ÁêÝñáéï õðüëïéðï"
    print "6. dinami"
    print "7. ¸telos"
    
    ans=raw_input("What would you like to do?")
    if ans!="7":
        ar1 = int(input("dwse arithmo1:"))
        ar2 = int(input("dwse arithmo2:"))
    
    #1
    if ans=="1":
        print "\n prosthesi Added"
        x = ar1+ar2
        print x
    #2    
    elif ans=="2":
        print "\n .aferesi"
        y =  ar1-ar2
        print y
    #3    
    elif ans=="3":
        print "\n pollaplasiasmos"       
        z =   ar1*ar2
        print z
    #4    
    elif ans=="4":
        print "\n dieresi"
        if ar2>0:
            o = ar1/ar2
            print o
    #5            
    elif ans=="5":
        print "\n ÁêÝñáéï õðüëïéðï"
        if ar2>0:
            p = ar1%ar2
            print p
    #6        
    elif ans=="6":
        print "\n dinami"
        k =   ar1**ar2
        print k
    #7    
    if ans =="7":
        print "TELOS"

#askisi me MENU

ans=1

while ans!="7":
    print "1.��������"
    print "2.��������"
    print "3. ���������������"
    print "4. ��������"
    print "5. ������� ��������"
    print "6. ��������"
    print "7. ������"
    
    ans=raw_input("What would you like to do?")
    if ans!="7":
        ar1 = int(input("dwse arithmo1:"))
        ar2 = int(input("dwse arithmo2:"))
    
    #1
    if ans=="1":
        print "\n �������� Added"
        x = ar1+ar2
        print x
    #2    
    elif ans=="2":
        print "\n .��������"
        y =  ar1-ar2
        print y
    #3    
    elif ans=="3":
        print "\n ���������������"       
        z =   ar1*ar2
        print z
    #4    
    elif ans=="4":
        print "\n ��������"
        if ar2>0:
            o = ar1/ar2
            print o
    #5            
    elif ans=="5":
        print "\n ������� ��������"
        if ar2>0:
            p = ar1%ar2
            print p
    #6        
    elif ans=="6":
        print "\n ��������"
        k =   ar1**ar2
        print k
    #7    
    if ans =="7":
        print "TELOS"

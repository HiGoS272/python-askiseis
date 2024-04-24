#ασκηση με δομή επανάληψης 

ar = raw_input("dwse ariumo kikloforias:")
c = 0
while ar!="*":


    time = int(input("dwse diarkia stathmeusis:"))
    while time >0:
        time = int(input("dwse diarkia stathmeusis:"))

    if time <=4:
        x = 2.5*time
    elif time > 4 and time <=7:
        x = 2.5*4 + (time - 4)*2
    else:
        x=2.5*4 + 3*2 + (time - 7)*1.5
        
        
    print ar,x

    if time<=3:
        c=c+1
        




    ar = raw_input("dwse ariumo kikloforias:")

print c

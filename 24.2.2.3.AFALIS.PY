while True:
    n = int(input("Δώσε Τριψήφιο Αριθμό:"))
    

    #Εκκατονταδες:
    a = n/100
    num1=int(str(a)[0])
    #Δεκαδες:
    b = (n%100) / 10
    num2=int(str(b)[0])
    #Μοναδες:
    c = (b%100) %10
    num3=int(str(c)[2])

    print("Πρώτος Αριθμός:") 
    #1o αριθμος:
    print(num1,":")
    print("Δεύτερο Αριθμός:")
    #2o αριθμος:
    print(num2,":")
    print("Τρίτο Αριθμός:")
    #3o αριθμος:
    print(num3,":")
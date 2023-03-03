 #Να γράψετε πρόγραμμα το οποίο θα διαβάζει τις 3 θερμοκρασίες από μια city.Με τη βοήθεια μια Fuction θα υπολογίζεται και θα επιστρέφει την Μέση Τιμή της θερμοκρασίας. 
 #Στη συνεχεία θα φτιάξετε μια ακομά Fuction η οποία θα εμφανίζει το μήνυμα (Frozen) αν η Μέση Τιμή είναι κάτω απο 0, το μήνυμα (Hot) αν η  Μέση Τιμή είναι απο 35 βάθμους 
 #και πάνω , και στις υπόλοιπες περιπτόσεις να εμφάνιζει το μήνυμα (Normal). 


while True:


    a1 = int(input("Dwse 1η Thermokrasia:"))
    a2 = int(input("Dwse 2η Thermokrasia:"))
    a3 = int(input("Dwse 3η Thermokrasia:"))

    def thermokrasia1(a1, a2, a3):
        mesiTimi= (a1 + a2 + a3)/3
        return  mesiTimi
    def thermokrasia2(mesiTimi):
        if mesiTimi < 0:
            print("Frozen")
        elif mesiTimi >= 35:
            print("Hot")
        else:
            print("Normal")        
    mesiTimi=thermokrasia1(a1, a2, a3)
    thermokrasia2(mesiTimi) 

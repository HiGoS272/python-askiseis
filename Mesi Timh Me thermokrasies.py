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

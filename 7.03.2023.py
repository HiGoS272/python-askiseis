#Να γράωετε μια συνάρτηση η οποία θα ελέγχει αν μια συμβολοσειρά αποτελεί ηλεκτρονική διευθυνσή αλληλογραφίας ελληνικού ιστοτοπου, Δλδ περιεχεί το συμβολο "@", δεν περιέχει κενά και έχει κατάληξη (.gr) 

while True:

    def myFuction(demo):
        if "@" in demo and demo[-1]=="r"and demo[-2]=="g" and demo[-3]=="." and demo[-4]=="@":
                return True
            
        else:
            return False

    a = input("Grapse kati:")
    print(myFuction(a))        

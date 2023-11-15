#EKFONISI:

# Ενα laptop κωστιζει 490€, και ο πολιτης μας δινει εκπτωση 15%.  
# Σε μια συναρτηση να υπολογιστει και να επιστρεψει την εκπωση του προΪοντος
# Σε μια αλλη συναρτηση να επισταφει και τα υπολογιστει Το ΦΠΑ 13%. 
# Επιτα θα υπολογιστει και θα υπολογιζει τη καθαρη τιμη του laptop 22 % 

#Τι έχουμε:

# proion 490
# ekptosi 15%
# fpa 13%

#Τι ζήταει

timiProion = int(input("dwse thn timi tou prohntos:"))
#1
def timiMeEkptosi(timiProion):


    ekptosi = (timiProion * 15) / 100
    return ekptosi

var = timiMeEkptosi(timiProion)
print("1) H Ektposi einai : ", str(var))

telikiTimi = timiProion - var
print("2) H teliki timi tou prohontos me Ektposi  einai : ", str(telikiTimi))

#2
def fpa(timiProion):

    upolFpa = (timiProion * 13)/100
    return upolFpa

var2 = fpa(timiProion)
print("3) To fpa einai : ", str(var2))

telikiTimiFpa = timiProion - var2
print("4) H teliki timi tou prohontos einai : ", telikiTimiFpa)

#3
def forosIsodimatos(var2):

    forosIsod = (var2 * 22) / 100
    return forosIsod

var3 = forosIsodimatos(var2)
print("5) O Foros Isodimatos Einai : ", str(var3))

telikiTimiMeForoIsodimatos = telikiTimiFpa - var3
print("6) teliki Timi Me Foro Isodimatos einai : ",telikiTimiMeForoIsodimatos)

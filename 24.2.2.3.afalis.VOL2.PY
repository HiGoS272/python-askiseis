while True:
 
    names = input("Give A Name:")
    c = 1
    def onomata(c ,names):
        for x in range(3):
            print (c ,names)
            c = c + 1

    onomata(c ,names)


    def onomata2(x1):
        c = 4
        onomata(c ,names)
        c = 7
        onomata(c ,names)

    onomata2(names)
     
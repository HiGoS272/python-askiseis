class Apothiki:

    def __init__(self, ogkos):
        self.ogkos = ogkos
        
    def eisagogi (self, kivotio):
        self.ogkos += kivotio

    def ejagogi(self, kivotio):
        self.ogkos -= kivotio

    def emfanise(self):
        print "Xwros =", self.ogkos


apothiki = Apothiki (1500)

apothiki.eisagogi(200)
apothiki.eisagogi(300)
apothiki.emfanise()
apothiki.ejagogi(200)
apothiki.emfanise()


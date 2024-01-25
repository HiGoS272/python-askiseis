class laptop:

    def __init__( self, model, inches,kg):

        self.model = model
        self.inches = inches
        self.kg = kg
        
    def emfanisiTwnTimwn (self):

         print self.model
         print self.inches
         print self.kg

propertis = laptop("LP", 15.6, 2.7)

print propertis.emfanisiTwnTimwn()

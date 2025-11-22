class country:

    def __init__(self,name):
        self.name=name

    def capital(self):
        pass

    def language(self):
        pass

class india(country):
    
    def capital(self):
        print("Capital: New Delhi")

    def language(self):
        print("Language: Tamil")

class usa(country):

    def capital(self):
        print("capital: london")

    def language(self):
        print("Language: English")


class uk(country):

    def capital(self):
        print("capital: japan")

    def language(self):
        print("Language: japnese")


countries=[india("India"), usa("USA"), uk("Uk")]

for c in countries:
      print("\nCountry Name:", c.name)
      c.capital()
      c.language()
      


class bird:

    def __init__(self,name):
        self.name=name
        
    def make_sound(self):
        print("some birds sound")

class parrot(bird):
        
    def make_sound(self):
        
        print(f"{self.name} says: kiii kiiii")

class sparrow(bird):

        
    def make_sound(self):
        print(f"{self.name} says: kuk kuk")

b1=parrot("parrot")
b2=sparrow("sparrow")

b1.make_sound()
b2.make_sound()


        
        

#Inheritance Example
#parrent Class
class Vehical:
    def __init__(self, M,C):
        
        self.milleage = M
        self.Cost = C

    def show_vehical_details(self):
        print("i am a vehicale")
        print("Milege of vehicale is", self.milleage)
        print("Cost of vehicale is", self.Cost)

v1 = Vehical(10000,600)

#v1.show_vehical_details()

#chiled class
# class car(Vehical):
#     def show_car_details(self):
#         print("my car")

# c1 = car(200,12000)

# c1.show_vehical_details()

#Over-riding init method

class Car(Vehical):

    def __init__(self, M, C,tyres,hp):
        super().__init__(M, C)
        self.tyres=tyres
        self.hp = hp

    def show_details(self):
        print("i am a vehicale")
        print("Tyres of vehicale is", self.tyres)
        print("Hp of vehicale is", self.hp)


c1 = Car(200,100000,4,300)

c1.show_vehical_details
c1.show_details()

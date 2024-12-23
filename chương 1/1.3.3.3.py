# Khai báo lớp chim
class Bird:
    def flight(self): # Định nghĩa phương thức flight()
        print("Many birds can fly !")
#-----------------End class Bird---------------------------
#Khai báo lớp chim sẻ kế thừa từ lớp bird
class Sparrow(Bird):
    def flight(self):    # Ghi đè phương thức flight()
        print("Sparrow can fly!")
class Ostrich(Bird):
    def flight(self):
        print("Ostriches CAN NOT FLY !!!")
#-----------------End class Obstrich-----------------------
obj1 = Bird()
obj2 = Sparrow()
obj3 = Ostrich()
#----------------------------------------------------------
obj1.flight()
obj2.flight()
obj3.flight()


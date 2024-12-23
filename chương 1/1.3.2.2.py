class Zebra:   # Lớp cha 1
    def __init__(self):
        print("Zebra")
    def Display(self):
        print("I'm a Zebra")
#-------------------End of class Zebra------------
class Donkey:
    def __init__(self):
        print("Donkey")
    def Display(self):
        print("I'm a Donkey!")
#-------------------End of class Donkey-------------
class Zonkey(Zebra, Donkey):         #Lớp con Zonkey kế thừa lớp Zebra và Donkey
    def __init__(self):
        Zebra.__init__(self)
        Donkey.__init__(self)
        print("Zonkey")
#-------------------End of class Zonkey------------
obj = Zonkey()
obj.Display()
# Đổi chỗ zebra vs donkey dòng 13
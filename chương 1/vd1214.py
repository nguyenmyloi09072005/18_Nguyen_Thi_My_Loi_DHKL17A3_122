#Ví dụ demo về constructor (hàm tạo) có tham số
class Dog:
    #Constructor CÓ tham số
    def __init__ (self, name):
        print("Đây là Constructor có tham số")
        self.name = name
    
    def display(self):
        print("Hello", self.name)
#-------------End class Dog--------------------------
bull = Dog("The Dom")
bull.display()
        
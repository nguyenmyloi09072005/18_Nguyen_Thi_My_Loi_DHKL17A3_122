# Ví dụ demo về constructor (hàm tạo) không có tham số
class Dog:
    #Constructor KHÔNG CÓ tham số
    def __init__(self):
        print('Đây là constructor KHÔNG CÓ tham số!')
    def display(self,name):
        print("Hello",name)
bull = Dog()
bull.display("The Dom")       
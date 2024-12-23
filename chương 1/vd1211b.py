class Myclass:
    def __init__(self,value):
        self.value = value

    def my_method(self):
        print('Giá trị của đối tượng là:',self.value)
#------------End lớp Myclass--------------------------
obj = Myclass(50)  #khai báo và khởi tạo một đối tượng obj từ lớp Myclass
# gọi phương thức Myclass 
obj.my_method()
#Phương thức hủy (destructor)
#là phương thức hủy đối tượng 
# không cần thiết vì trong py theo cơ chế tự động qli bộ nhớ
#(tự động hủy đối tượng khi k sdung)
#-------------------------------------------------------------

class Cat:
    #khai báo thuộc tính
    def __init__(self,name,size,color,age):
        self.name = name
        self.size = size
        self.color = color
        self.age = age
    def __del__(self):
        print("A Cat object is being deleted")

obj = Cat("Kitty","mini",1,"pink")
del obj    
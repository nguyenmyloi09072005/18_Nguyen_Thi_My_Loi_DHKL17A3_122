class Dog:     #ví dụ DEMO về phương thức dựng sẵn của lớp

    DogCount = 0 #thuộc tính của lớp/class
    #Hàm khởi tạo đối tượng
    def __init__(self, name, size, age, color):
        self.name = name  #Thuộc tính của đối tượng (object)
        self.size = size
        self.age = age
        self.color = color
#-------------End class Dog----------------------------
#Tạo ra đối tượng của lớp Dog
bull = Dog('Bull', 'large', 2, "yellow")
#In ra thuộc tính name của đối tượng Bull
print(getattr(bull,'name'))
# gán giá trị của age cho 3
setattr(bull,'age',3)
#in ra giá trị của age
print(getattr(bull,'age'))
# true nếu bull chứa thuộc tính large
print(hasattr(bull,'large'))
# xóa thuộc tính age
delattr(bull,'large')
#kích hoạt lỗi nếu age đã bị xóa
print(bull.age)

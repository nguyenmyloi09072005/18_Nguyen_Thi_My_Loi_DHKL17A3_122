class Dog:    
    # thuộc tính lớp
    DogCount = 0 #thuộc tính của lớp/class
    #Hàm khởi tạo đối tượng
    def __init__(self, name, size, age, color):
        self.name = name  #Thuộc tính của đối tượng (object)
        self.size = size
        self.age = age
        self.color = color
        Dog.DogCount=Dog.DogCount + 1
    @staticmethod
    def Report():
        print("Tổng số đối tượng Dog: {}".format(Dog.DogCount))
    
#------------------------------End class Dog---------------------------
doc1 = Dog("Buddy", "medium", 5, "brown")
doc2 = Dog("Max", "small", 3, "black")
# sử dụng phương thức tĩnh Report() để lấy/báo cáo số lượng đối tượng Dong đã đc tạo ra
doc1.Report()
class Dog:    
    # thuộc tính lớp
    DogCount = 0 #thuộc tính của lớp/class
    #Hàm khởi tạo đối tượng
    def __init__(self, name, size, age, color):
        self.name = name  #Thuộc tính của đối tượng (object)
        self.size = size
        self.age = age
        self.color = color
    @classmethod
    def CreateDog(cls, name, size, age, color): #phương thức lớp
        cls.DogCount =  cls.DogCount + 1
        return cls(name, size, age, color)
    @classmethod
    def get_dog_count(cls):  # phương thức lớp
        return cls.DogCount
#------------------------------End class Dog---------------------------
obj1 = Dog.CreateDog("Bull", "large", 2, "yellow")
print("Số lượng đối tượng đã được tạo ra là:",Dog.get_dog_count())
obj2 = Dog.CreateDog("Bull", "large", 2, "yellow")
print("Số lượng đối tượng đã được tạo ra là:",Dog.get_dog_count())

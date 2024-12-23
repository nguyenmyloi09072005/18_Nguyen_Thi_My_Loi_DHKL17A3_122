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
    
    def __del__(self):
        print("A dog object is being deleted!!!")
        Dog.Dogcount = Dog.DogCount -1
#------------------------------End class Dog---------------------------
# Tạo các đối tượng Dog
doc1 = Dog("Buddy", "medium", 5, "brown")
doc2 = Dog("Max", "small", 3, "black")

print("Number of dogs: {}".format(Dog.DogCount))
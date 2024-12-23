class Dog:

    DogCount = 0 #thuộc tính của lớp/class
    #Hàm khởi tạo đối tượng
    def __init__(self, name, size, age, color):
        self.name = name  #Thuộc tính của đối tượng (object)
        self.size = size
        self.age = age
        self.color = color
    def Go(self):
        print('Im going ...')     #Hành vi/hoạt động "đi"
    
    def Stay(self, place):
        print("I'm staying at {}".format(place))
    
    def Lie(self, place):
        print(" I'm lying at {}".format(place))

    def Bark(self):
        print("whoop,...")

    def Eat(self,food):
        print("I'm eating {}".format(food))
#-------------------------End class Dog--------------------------------
# khởi tạo đối tượng
bull = Dog("Bull","large","2","yellow")
bull.Stay("Garden")
bull.Bark()
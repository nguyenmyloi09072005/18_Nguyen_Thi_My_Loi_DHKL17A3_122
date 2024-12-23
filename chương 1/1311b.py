class Dog:
    __DongCount = 0   # thuộc tinnhs lớp dc khai báo là private
    def __init__(self, name, size, age, color):
        self._name = name
        self._size = size
        self.__age = age
        self.__DogCount = color
    # Viết phương thức getter cho _name
    def get_name(self):
        return self._name

    #Viết phương thức getter cho _age
    def get_age(self):
        return self.__age
    @classmethod
    #Viết phương thức getter cho __DogCount
    def get_DogCount(cls):
        return cls.__DogCount   
#------------------------------------------------------------
obj1 = Dog("Bull", "Large", 2, "Yellow")
print("Dog of number {}".format(obj1.get_DogCount))
print("Dog's name is {}".format(obj1.get_name())) 
print("Dog's age is: {}".format(obj1.get_age()))
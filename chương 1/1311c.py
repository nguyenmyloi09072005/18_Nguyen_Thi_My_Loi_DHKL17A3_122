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
    
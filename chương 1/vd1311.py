class Dog:     #ví dụ minh họa về ENCAPSULATION
    #thuộc tính của lớp/thuộc tính tĩnh
    __DogCount = 0    #DocCount là thuộc tính private
    def __init__(self, name, size, age, color):
        self.name = name  #Thuộc tính của đối tượng (object)
        self.size = size
        self.age = age
        self.color = color
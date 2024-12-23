# Xây dựng lớp phân số
class PS:
    def __init__(self):
        self.x = 0
        self.y = 1
    def nhap_PS(self):
        self.x = float(input('Nhập vào tử số:'))
        self.y = float(input('Nhập vào mẫu số:'))
    def ktra_PS(self):
        if self.y==0:
            print('Không hợp lệ')
        else:
            print(f'phân số là:{int(self.x)}/{int(self.y)}')
#tạo đối tượng            
phan_so = PS()
phan_so.nhap_PS()
phan_so.ktra_PS()



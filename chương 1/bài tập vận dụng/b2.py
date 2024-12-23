# quản lí điểm thi
class sinh_vien:
    def __init__(self,ho_ten,diem_toan,diem_ly,diem_hoa):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa
    
    def in_ra_tt(self):
        print('thông tin thí sinh:Họ và tên:%s,Điểm toán:%d,Điểm lý:%d,Điểm hóa :%d'%(self.ho_ten,self.diem_toan,self.diem_ly,self.diem_hoa))
    def tong_diem(self):
        return (self.diem_toan + self.diem_ly + self.diem_hoa)
danh_sach = []
so_luong_sv = int(input('nhập vào số lượng sinh viên:'))
for i in range(so_luong_sv):
    print(f'nhập thông tin sinh viên thứ :{i+1}')
    ten = input('Nhập vào tên sinh viên:') 
    diemtoan = int(input('nhập vào điểm toán:'))
    diemly = int(input('nhập vào điểm lý:'))    
    diemhoa = int(input('nhập vào điểm hóa:'))
    tt_sv= sinh_vien(ten
,diemtoan,
diemly,
diemhoa)
    # tt_sv.in_ra_tt()   
    # td = tt_sv.tong_diem()
    danh_sach.append(tt_sv)
print('\nThông tin và tổng điểm của tất cả sinh viên:')
soluong = 0
for sv in danh_sach:
    sv.in_ra_tt()  # In thông tin sinh viên
    tongdiem = sv.tong_diem()
    if tongdiem >20:
        print('DO')
    else:
        print('TRUOT') 
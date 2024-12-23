#lớp biểu diễn hình chữ nhật
class hcn:
   def __init__(self, chieu_dai, chieu_rong):
      self.chieu_dai = chieu_dai
      self.chieu_rong = chieu_rong
   def chu_vi_hcn(self):
      return 2*(self.chieu_dai + self.chieu_rong)
   def dien_tich_hcn(self):
      return self.chieu_dai * self.chieu_rong
chieu_dai = float(input("Nhập vào độ dài:"))
chieu_rong = float(input("Nhập vào độ dài:"))
   
# Tạo đối tượng hcn
hinh_chu_nhat = hcn(chieu_dai, chieu_rong)

# In chu vi và diện tích
print("Chu vi hình chữ nhật là:", hinh_chu_nhat.chu_vi_hcn())
print("Diện tích hình chữ nhật là:", hinh_chu_nhat.dien_tich_hcn())

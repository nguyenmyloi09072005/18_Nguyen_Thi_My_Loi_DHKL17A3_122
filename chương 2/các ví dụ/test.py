import requests
#thực hiện yêu cầu HTTP đến địa chỉ URL 'https://https://jsonplaceholder.typicode.com/pots'ArithmeticError
response = requests.get('https://https://jsonplaceholder.typicode.com/pots')
# Kiểm tra xem yêu cầu có OK không
if response.status_code == 200:
   # Nếu yêu cầu thành công thì lấy dữ liệu từ Json từ phản hồi
   json_data = response.json()

   #In ra màn hình thông tin các bài đăng từ dữ liệu Json cuẩ trang web
   for post in json_data:
      print("ID") 
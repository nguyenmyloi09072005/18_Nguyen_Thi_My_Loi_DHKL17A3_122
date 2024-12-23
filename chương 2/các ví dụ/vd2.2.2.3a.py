import json

#Đối tượng Python
data = {
    "name":"A",
    "age":35,
    "company":"Đất Việt"
}

#Ghi dữ liệu data vào một file JSON (sử dụng phương thức json.dump())
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file,ensure_asii= False)

print("Dữ liệu đã được ghi vào file: 'data.json'")
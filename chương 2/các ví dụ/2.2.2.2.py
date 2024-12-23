import json
json_string_1 = '{"name":"A","age":35,"company":"Đất Việt"}'
json_string_2 = "{\"name\": \"A\", \"age\": 35, \"company\": \"Đất Việt\"}"

#Chuyển đổi chuỗi Json thành đối tượng trong Python
json_object_1 = json.loads(json_string_1)
json_object_2 = json.loads(json_string_2)

print(json_object_1)
print(json_object_2)

print(type(json_object_1))

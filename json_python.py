import json

json_data = '{"name": "Ivan", "age": 30, "is_student": false}'
parsed_data = json.loads(json_data)
print(parsed_data['name'])

data = {
    "name": "Maria",
    "age": 35,
    "is_student": True,
}
json_string = json.dumps(data, indent=4)
print(json_string)

with open("json_example.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    print(data, type(data))
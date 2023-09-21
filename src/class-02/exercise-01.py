import json

def convert_dict(data):
    json_str = json.dumps(data)
    print(json_str)
    new_dict = json.loads(json_str)
    print(new_dict)
    return new_dict

my_data = { "name": "John", "age": 30, "city": "New York"}
convert_dict(my_data)
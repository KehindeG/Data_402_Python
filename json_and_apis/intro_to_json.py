import json

car_data = {
    "name": "Tesla",
    "engine": "electric"
}

print(car_data)

# json.dumps() --> turn python dict to a str
car_data_string = json.dumps(car_data)
print(type(car_data_string))

# json.dump() --> converts a dict to a str AND outs it in a new file
with open("new_json_file.json", "w") as jsonfile:
    json.dump(car_data, jsonfile)

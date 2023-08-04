import json 

#1st going to check if the string is valid or not 
def is_valid_json(json_str):
    try:
        json.loads(json_str)
        return "The input is a valid Json string"
    except ValueError:
        return "The input is not a valid Json string"

#2nd is a valid list in the string
def convert_list_strings(obj):
    for key, value in obj.items():
        if isinstance(value, str):
            if value.startswith("[") and value.endswith("]"):
                try:
                    obj[key] = [i for i in value.strip('[]').split(',') if i.strip()]
                except ValueError:
                    pass
    return obj

def parser(json_string):
    if is_valid_json(json_string):
        json_data = json.loads(json_string , object_hook=convert_list_strings)
        #converting all the string to into and float
        for key , value in json_data.items():
            if isinstance(value, str):
                if value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
                    json_data[key] = int(value)
                elif value.replace('.', '', 1).isdigit() or (value.startswith('-') and value[1:].replace('.', '', 1).isdigit()):
                    json_data[key] = float(value)
        #converting all thelist items to int or float 
        for key , value in json_data.items():
            if isinstance(value, list):
                temp = []
                for i in value:
                    if isinstance(i, str):
                        if i.isdigit() or (i.startswith('-') and i[1:].isdigit()):
                            temp.append(int(i))
                        elif i.replace('.', '', 1).isdigit() or (i.startswith('-') and i[1:].replace('.', '', 1).isdigit()):
                            temp.append(float(i))
                json_data[key] = temp
    return json_data

json_string = '{"name": "Chaitanya", "age": "22", "rating": "122.948", "list" : "[1,2,3,4,5]" , "str_list" : ["1", "2", "3"]}'
parsed_object = parser(json_string)
print(parsed_object)
import json #JSON - JavaScript Object Notation


data = {
    "user" : {
        "id" : 1,
        "login" : "asdvz",
        "password" : 218321,
        "is_active" : True,
        "qwe" : None,
    },
    "interests" : ["sport", "age", "code"]
}


with open("file.json" , "w") as fhand_js:
    json.dump(data, fhand_js, indent=4)


with open("file.json", "r") as fhand_js:
    new_data = json.load(fhand_js)

print(new_data)
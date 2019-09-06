import simplejson as json
import os

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
    oldFile = open("./ages.json", "r+")
    data = json.loads(oldFile.read())
    print("Current age is ", data["age"], "--- adding year.")
    data["age"] = data["age"] + 1
    print("New age is : ",data["age"])
else:
    oldFile = open("./ages.json", "w+")
    data = {"name": "Nick",
            "age": 20}

    print("No file found, setting default age to ", data["age"])

oldFile.seek(0)
oldFile.write(json.dumps(data))
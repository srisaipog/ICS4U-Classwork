path = "home/robuntu/Sairam/ICS4U-Classwork/learning_python/"

path = ""

import json

appDict = {
    "name": "messenger",
    "playstore": True,
    "company": "Facebook",
    "price": 100
}

app_json = json.dumps(appDict) # dump string

# later load string to pull 

print(type(app_json))
print(app_json)
print(type(appDict))
print(appDict)

f_name = "blip_blip.json"

new_stuff = []

with open(path + f_name, 'w') as u:
    u.write(app_json)
    json.dump(app_json, u)

with open(path + f_name, 'r') as k:
    new_stuff.append(k.read())
    new_stuff.append(json.load(k))
    #new_stuff.append(json.load(k,'s'))

print(new_stuff)
import json
file=open("ranking.json","r")
dict=json.load(file)
print(dict)
for i in dict:
    print(dict[i])
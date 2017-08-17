import json
with open('a.json', 'r') as f:
    json_data = f.readlines()

    for i in json_data:
        json_dict = json.loads(i)
        if json_dict["title"]==u"イギリス":
            print(json_dict["text"])
            break

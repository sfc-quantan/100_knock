# -*- coding: utf-8 -*-
import json

with open('a.json', 'r') as f:
    json_load = f.readline()
    while json_load:
        json_article = json.loads(json_load)
        if json_article["title"] == u"イギリス":
            for line in json_article["text"].split("\n"):
                if "Category" in line:
                    print(line.replace('Category', ''))
        json_load = f.readline()

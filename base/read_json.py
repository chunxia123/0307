import json
def read_json():
    with open("./data/test.json","r",encoding="utf-8") as f:
        data=json.load(f)
        list=[]
        for ele in data.values():
            list.append(ele)
        return list
import yaml
def read_yaml(testcasenum,filename):
    with open("./data/"+filename,"r") as f:
        data=yaml.load(f, Loader=yaml.FullLoader)
        data2=data[testcasenum]
        list_data=list()
        for ele in data2.values():
            list_data.append(ele)
        return list_data
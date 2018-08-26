import yaml
def get_data():
    with open("../Data/address_data.yml",'r',encoding="utf-8") as f:
        return yaml.load(f)
if __name__ == '__main__':
    datas=get_data().get("edit_address")
    # print(datas.values())
    for data in datas.values():
        print(data)
import os
import yaml
class ReadYml():
    def __init__(self,filename):
        self.filepath=os.getcwd()+os.sep+"Data"+os.sep+filename
    def read_yml(self):
        with open(self.filepath,"r",encoding="utf-8") as f:
            return yaml.load(f)

# if __name__ == '__main__':
    # print(ReadYml("login_data.yml").read_yml())
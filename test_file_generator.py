import os
import json
import random

# This script generates 20 test files with the naming format of x.json
# For example 0.json, 1.json... 19.json, 20.json
# The data in these files is a simple object with an index, and some random data

class RandData:
    def __init__(self, index):
        self.index = index
        self.data = random.randint(1, 100)

datas = []

for i in range(20):
    myClass = RandData(i)
    datas.append(myClass)

random.shuffle(datas)
for data in datas:
    file_name = str(data.index) + ".json"
    out = json.dumps(data.__dict__)
    with open(os.path.join("files", file_name), mode='w') as f:
        f.write(out)

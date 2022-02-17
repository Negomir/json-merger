import os
import json
import glob

print(__file__)

data = []
indexes = []
datas = dict()

output = []

# Iterating over files and from each file name getting it's index
# I am storing these indexes into a list, so that I can easily sort them
# I am also making a dict of index:data so that once I am going over the sorted indexes I can easily access the data of that index file
for file in glob.glob(r".\files\*.json"):
    print(file)
    with open(file, mode='r') as f:
        ind = int(f.name.split(".\\files\\")[1].split(".json")[0]) #Splitting the file name to get the index. Can also be achieved by loading the json and getting the index value.
        indexes.append(ind)
        datas[ind] = json.loads(f.read())

# Iterating over sorted file indexes and adding their data to the output list
for ind in sorted(indexes):
    output.append(datas[ind])

# Writing the output list
out = json.dumps(output)
with open("output_file.json", mode='w') as f:
    f.write(out)

import os

print(os.listdir("files"))

for filename in os.listdir("files"):
    file_path = os.path.join("files", filename)
    with open(file_path, "r") as f:
        print(file_path, ": ", f.read())

import re

string = "这是我的主页 https://mofanpy.com, 这个 www.mofanpy.com 有很多 mofan 教你机器学习和 python 语言的教学"
res = re.findall(r"(https://)?(mofanpy.com)", string)
for r in res:
    print(r[1])

for filename in os.listdir("files"):
    file_path = os.path.join("files", filename)
    with open(file_path, "r") as f1:
        string = f1.read()
        new_string = re.sub(r"morvanzhou.github.io", "mofanpy.com", string)
        with open(os.path.join("files", "new_" + filename), "w") as f2:
            f2.write(new_string)
for filename in os.listdir("files"):
    if filename.startswith("new_"):
        continue
    file_path = os.path.join("files", "new_" + filename)
    with open(file_path, "r") as f:
        print(file_path, ": ", f.read())




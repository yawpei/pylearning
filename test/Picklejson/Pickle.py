import os
import pickle

data = {"aaa": 1, "bbb": 2, "ccc": 3}
print(pickle.dumps(data))

data = {"filename": "f1.txt", "create_time": "today", "size": 111}
with open("data.pkl", "wb") as f:
    print(pickle.dump(data, f))
print(os.listdir())

with open("data.pkl", "rb") as f:
    data = pickle.load(f)
    print(data)


class File:
    def __init__(self, name, create_time, size):
        self.name = name
        self.create_time = create_time
        self.size = size


data = File("f2.txt", "now", 222)
# 存
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)
# 读
with open("data.pkl", "rb") as f:
    read_data = pickle.load(f)
print(read_data.name)
print(read_data.size)

#################
# 注意，可能是浏览器的原因，点击运行后会报错，但是在正常的 Python 执行环境中，
# 运行是没有问题的，运行结果如下：
#################
"""
f2.txt
222
"""


class File:
    def __init__(self, name, create_time, size):
        self.name = name
        self.create_time = create_time
        self.size = size
        self.file = open(name, "w")


# data = File("f3.txt", "now", 222)
# # pickle 存，会报错
# with open("data.pkl", "wb") as f:
#     pickle.dump(data, f)

#################
# 注意，可能是浏览器的原因，点击运行后会报错，
# 我们知道它会报错，但是报的错不是它说的那样，而是下面这样：
#################
"""
Traceback (most recent call last):
  File "<input>", line 11, in <module>
TypeError: cannot pickle '_io.TextIOWrapper' object
"""


class File:
    def __init__(self, name, create_time, size):
        self.name = name
        self.create_time = create_time
        self.size = size
        self.file = open(name, "w")

    def __getstate__(self):
        # pickle 出去需要且能被 pickle 的信息
        pickled = {"name": self.name, "create_time": self.create_time, "size": self.size}
        return pickled

    def __setstate__(self, pickled_dict):
        # unpickle 加载回来，重组 class
        self.__init__(
            pickled_dict["name"], pickled_dict["create_time"], pickled_dict["size"])


data = File("f3.txt", "now", 222)
# 存
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)
# 读
with open("data.pkl", "rb") as f:
    read_data = pickle.load(f)
print(read_data.name)
print(read_data.size)

#################
# 注意，可能是浏览器的原因，点击运行后会报错，
# 在正常的 Python 环境中，结果如下：
#################
"""
f3.txt
222
"""

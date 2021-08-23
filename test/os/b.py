import os
import shutil

if os.path.exists("user/mofan/a.txt"):
    print("user exist")
else:
    os.makedirs("user/mofan", exist_ok=True)
    with open("user/mofan/a.txt", "w") as f:
        f.write("nothing")
        f.close()

if os.path.exists("user/mofan"):
    print(os.listdir("user"))
else:
    shutil.rmtree("user/mofan")
    print(os.listdir("user"))

if os.path.exists("user/mofan"):
    print(os.listdir("user"))
else:
    os.makedirs("user/mofan", exist_ok=True)
    os.rename("user/mofan", "user/mofanpy")
    print(os.listdir("user"))

# import oshttps://mofanpy.com/support/
# os.makedirs("user/mofan", exist_ok=True)
# with open("user/mofan/a.txt", "w") as f:
#     f.write("nothing")
print(os.path.isfile("user/mofanpy/a.txt"))  # True
print(os.path.exists("user/mofanpy/a.txt"))  # True
print(os.path.isdir("user/mofanpy/a.txt"))  # False
print(os.path.isdir("user/mofanpy"))  # True

import os


def copy(path):
    filename = os.path.basename(path)  # 文件名
    dir_name = os.path.dirname(path)  # 文件夹名
    new_filename = "new_" + filename  # 新文件名
    return os.path.join(dir_name, new_filename)  # 目录重组


print(copy("user\\mofan\\a.txt"))


def copy(path):
    dir_name, filename = os.path.split(path)
    new_filename = "new_" + filename  # 新文件名
    return os.path.join(dir_name, new_filename)  # 目录重组


print(copy("user\\mofan\\a.txt"))

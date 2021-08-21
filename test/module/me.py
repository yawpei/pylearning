# me.py
# import file
#
# print(file.create_name())

# import file as f1
#
# print("f1:", f1.create_name())


# class File:
#     def create_name(self):
#         return "new file.txt"
#
#
# f2 = File()
# print("f2:", f2.create_name())


# from file import create_name
#
# print(create_name())


# 第一种，之前介绍了
import file

print("1", file.create_name())

# 第二种更偷懒
from file import *

print("2", create_name())
print("2", create_time())

import files.text

print(files.text.create_name())

# 或者这样：
from files import text

print(text.create_name())

from files import get_video_size

print(get_video_size())

a = "这就是 莫烦Python 交互式编辑器"
print(a)

print("=======", "变量", "=======>")
name = "文件管理系统"
print("莫烦Python最棒~")
print(name)
print("莫烦Python的", name, "业界顶呱呱")
print("我看着", "莫烦", "的教学长大的~")
print("<=======", "变量", "=======")

print("=======", "数学运算", "=======>")
a = 1
a += 1
print("a += ", a)
a -= 1
print("a -= ", a)
a *= 10
print("a *= ", a)
a /= 2
print("a /= ", a)

b = 100
b %= 21
print("取模")
print("b %=", b)

c = 3
c **= 2
print("幂")
print("c **=", c)

d = 100
d //= 21
print("取整除（取余）")
print("d //=", d)
print("<=======", "数学运算", "=======")

print("=======", "条件判断", "=======>")
in_trash = True
if in_trash:
    print("可以被彻底删除")
if not in_trash:
    print("不可以被彻底删除")

if in_trash:
    print("可以被彻底删除")
else:
    print("不可以被彻底删除")

print("2 < 3", 2 < 3)
print("3 < 2", 3 < 2)
print("2 != 2", 2 != 2)

print(2 < 3 and 2 < 5)
print(2 > 3 or 3 == 3)
print(2 > 3 or not 3 == 3 and 5 < 10)

a, b = 1, 2
if a > b:
    print("a 大于 b")
else:
    print("a 不大于 b")

today = 4
if today == 1:
    print("周一")
elif today == 2:
    print("周二")
elif today == 3:
    print("周三")
else:
    print("周一周二周三之外的一天")
print("<=======", "条件判断", "=======")

print("=======", "循环", "=======>")
print("==for")
for i in range(5):
    print("新文件-" + str(i))

for i in range(3, 10):
    print("新文件-" + str(i))
# 从3开始，一直到10之前，每2次出一次数
for i in range(3, 10, 2):
    print("新文件-" + str(i))

print("==while")
guess_num = 10
while guess_num != 20:
    guess_num += 1
    print(guess_num)

print("==and")
count = 0
guess_num = 30
while guess_num != 20 and count <= 10:
    guess_num -= 1
    count += 1
    print(guess_num)

print("==continue、break")
for i in range(10):
    if i % 2 == 0:
        continue  # 跳过偶数
    print(i)
for i in range(10):
    if i == 5:
        break
    print(i)

print("<=======", "循环", "=======")

print("=======", "数据种类", "=======>")
files = ["f1.txt", "f2.txt", "f3.txt", "f4.txt", "f5.txt"]
print("files[0] ", files[0])
print("files[3] ", files[3])
print("files[-1] ", files[-1])
print("files[-3] ", files[-3])
print("files[:3] ", files[:3])
print("files[2:4] ", files[2:4])
print("files[-3:] ", files[-3:])
print("old files[1] ", files[1])
files[1] = 12
print("new files[1] ", files[1])
l = [1, "file", ["2", 3.2]]
print(l)
l[2][0] = "new string"
print(l)
l[2][1] = "6.5"
print(l)
files = {"ID": 111, "passport": "my passport", "books": [1, 2, 3]}
print(files)
print(files["books"])
files["ID"] = 222
print(files)
files["ID"] = [2, 3, 4]
print(files)
# 元组有它一个唯一的独特性，就是它里面的东西不可变，定下来就定下来了，不让你变
files = ("file1", "file2", "file3")
print(files[1])
# files[1] = "file4"   # 这里会报错
my_files = set(["file1", "file2", "file3"])
print(my_files)
my_files.add("file3")
print(my_files)
my_files.add("file4")
print(my_files)
my_files.remove("file3")
print(my_files)

print("my_files", my_files)
your_files = {"file1", "file3", "file5"}
print("your_files", your_files)
print("交集 ", your_files.intersection(my_files))
print("并集 ", your_files.union(my_files))
print("补集 ", your_files.difference(my_files))

files = ["f1.txt", "f2.txt", "f3.txt", "f4.txt", "f5.txt"]
for i in range(len(files)):
    if files[i] == "f3.txt":
        print("I got f3.txt")
for f in files:
    if f == "f3.txt":
        print("I got f3.txt")

files = {"ID": 111, "passport": "my passport", "books": [1, 2, 3, 4]}
for key in files.keys():
    print("key:", key)
for value in files.values():
    print("value:", value)
for key, value in files.items():
    print("key:", key, "value:", value)

files = []
for i in range(5):
    files.append("f" + str(i) + ".txt")  # 添加
    print("has", files)
for i in range(len(files)):
    print("pop", files.pop())  # 从最后一个开始pop出
    print("remain", files)

files = ["f1.txt", "f2.txt"]

# 扩充入另一个列表
files.extend(["f3.txt", "f4.txt"])
print("extend", files)

# 按位置添加
files.insert(1, "file5.txt")     # 添加入第1位（首位是0）
print("insert", files)

# 移除某索引
del files[1]
print("del", files)

# 移除某值
files.remove("f3.txt")
print("remove", files)

files = {"ID": 111, "passport": "my passport", "books": [1,2,3]}

# 按key拿取，并在拿取失败的时候给一个设定好的默认值
print('files["ID"]:', files["ID"])
print('files.get("ID"):', files.get("ID"))

# 将另一个字典补充到当前字典
files.update({"files": ["1", "2"]})
print('update:', files)

# pop 调一个item，和列表的 pop 类似
popped = files.pop("ID")
print('popped:', popped)
print("remain:", files)
print("<=======", "数据种类", "=======")

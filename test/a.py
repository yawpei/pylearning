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

for i in range(3,10):
    print("新文件-"+str(i))
# 从3开始，一直到10之前，每2次出一次数
for i in range(3, 10, 2):
    print("新文件-" + str(i))

print("==while")
guess_num = 10
while guess_num !=20:
    guess_num+=1
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
        continue    # 跳过偶数
    print(i)
for i in range(10):
    if i == 5:
        break
    print(i)

print("<=======", "循环", "=======")


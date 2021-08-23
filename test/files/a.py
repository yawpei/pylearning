# 写文件
f = open("new_file.txt", "w")  # 创建并打开
f.write("some text...")  # 在文件里写东西
f.close()  # 关闭

with open("new_file2.txt", "w") as f:
    f.writelines(["some text for file2...\n", "2nd line\n"])

# 读文件
with open("new_file2.txt", "r") as f:
    print(f.readlines())

with open("new_file2.txt", "r") as f:
    while True:
        line = f.readline()
        print(line)
        if not line:
            break

with open("chinese.txt", "wb") as f:
    f.write("这是中文的，this is Chinese".encode("gbk"))

with open("chinese.txt", "rb") as f:
    print(f.read())

# 下面的代码会报错
with open("chinese.txt", "r") as f:
    print(f.read())

with open("chinese.txt", "r", encoding="gbk") as f:
    print(f.read())

# mode	意思
# w	（创建）写文本
# r	读文本，文件不存在会报错
# a	在文本最后添加
# wb	写二进制 binary
# rb	读二进制 binary
# ab	添加二进制
# w+	又可以读又可以（创建）写
# r+	又可以读又可以写, 文件不存在会报错
# a+	可读写，在文本最后添加
# x	创建

with open("new_file.txt", "r") as f:
    print(f.read())
with open("new_file.txt", "r+") as f:
    f.write("text has been replaced")
    f.seek(0)  # 将开始读的位置从写入的最后位置调到开头
    print(f.read())
with open("new_file.txt", "a+") as f:
    print(f.read())
    f.write("\nadd new line")
    f.seek(0)  # 将开始读的位置从写入的最后位置调到开头
    print(f.read())

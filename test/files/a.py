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

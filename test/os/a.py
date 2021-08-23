import os

print("当前目录：", os.getcwd())
print("当前目录里内容：", os.listdir())

os.makedirs("project", exist_ok=True)
print(os.path.exists("project"))

if os.path.exists("user/mofan"):
    print("user exist")
else:
    os.makedirs("user/mofan")
    print("user created")
print(os.listdir("user"))

if os.path.exists("user/mofan"):
    os.removedirs("user/mofan")
    print("user removed")
else:
    print("user not exist")

os.makedirs("user/mofan", exist_ok=True)
with open("user/mofan/a.txt", "w") as f:
    f.write("nothing")
    f.close()
os.removedirs("user/mofan")  # 这里会报错
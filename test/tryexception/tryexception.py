# with open("aaaa.txt", "r") as f:
#     print(f.read())

try:
    with open("aaaa.txt", "r") as f:
        print(f.read())
except FileNotFoundError as e:
    print(e)
    with open("aaaa.txt", "w") as f:
        f.write("I'm no_file.txt")
        print("new file 'no_file.txt' has been written")

d = {"name": "f1", "age": 2}
l = [1, 2, 3]
try:
    v = d["gender"]
    l[3] = 4
except (KeyError, IndexError) as e:
    print("key or index error for:", e)

d = {"name": "f1", "age": 2}
l = [1, 2, 3]
try:
    v = d["gender"]
    l[3] = 4
except KeyError as e:
    print("key error for:", e)
    d["gender"] = "x"
except IndexError as e:
    print("index error for:", e)
    l.append(4)
print(d)
print(l)

l = [1, 2, 3]
try:
    l[3] = 4
except IndexError as e:
    print(e)
finally:
    print("reach finally")


# try:
#     dddd = dddddd
# finally:
#     print("I know there is error, so what?")


# def no_negative(num):
#     if num < 0:
#         raise ValueError("I said no negative")
#     return num
#
#
# print(no_negative(-1))

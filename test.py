# _*_ coding : utf-8 _*_
# @Time : 2022/4/11 0:37
# @Author : gaohao
# @File : text
# @Project : demo

# num = 18
# boo = True
# str = "gaohao"
# print(len(str))
# print(str.find("g"))
# print(str.startswith("g"))
# print(str.endswith("g"))
# print(str.count("a"))
# print(str.replace("g","a"))
# print(str.split("a"))
# print(str.upper())
# print(str.lower())
# print(str.strip())
# print(str.join("aaaaaaaaaaaaaaa"))
# print(str[0:2:1])

lis = ["a", "b", "c"]
# print(lis.append("a"))
# print(lis.insert(1,"d"))
# print(lis.extend("d"))
# lis[1]="f"
# del lis[1]
# lis.pop()
# lis.remove("a")
# if "a" in lis:
#     print(lis)

# tup = (1, 2, 3)
# dic = {"name": "gaohao", "age": 18}
# for key in dic.keys():
#     print(key)
# for value in dic.values():
#     print(value)
# for key, value in dic.items():
#     print(key, value)
# dic["name"]="chuanyi"
# dic["sex"]="female"
# del dic["sex"]
# del dic
# dic.clear()
# print(dic.get("sex"))
# def main(str):
#     str = "mm"
#     return str
# ret = main(str)
# print(ret)

# fp = open("fp/test.txt", "w")
# fp = open("fp/test.txt", "a")
import json
# js = json.dumps(lis)
# fp.write(js)
# json.dump(lis, fp)
try:
    fp = open("fp/test.txt", "r")
    js=fp.read()
except FileNotFoundError:
    print("error")
finally:
    fp.close()
# print(type(js))
# print(type(json.loads(js)))
# print(json.load(fp))
# print(fp.readline())
# print(fp.readlines())


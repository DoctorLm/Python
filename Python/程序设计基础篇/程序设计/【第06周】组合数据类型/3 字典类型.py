d = {"中国":"北京", "美国":"华盛顿", "法国":"巴黎"}
print("中国" in d)

print(d.keys())
print(d.values())
print(d.get("常州","NO"))
print(d.get("中国","NO"))

d={}
d["a"] = 1; d["b"] = 2
d["b"] = 3

print("c" in d)
print(len(d))
print(d)
d.clear()
print(d)

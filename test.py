set1 = set()# 建立空的集合

set2 = {1, 2, 3, 4, 5}

# 從串列 (List) 來建立集合
set3 = set([i for i in range(20, 30)])

# 從數組 (Tuple) 來建立集合
set4 = set((10, 20, 30, 40, 50))

# 集合不會包含重複的資料, 你可以從 set5 印出來的結果得知
set5 = set((1, 1, 1, 2, 2, 3))

print(set1)
print(set2)
print(set3)
print(set4)
print(set5)

for e in set3:
    print(e, end = " ")
print("\n")
# Union intersection difference symmetric_intersection

uni_25 = set2.union(set5)
print(f"uni14 : {uni_25}\n")

inter_25 = set2.intersection(set5)
print(f"inter_25 : {inter_25}\n")

diff_25 = set2.difference(set5)
print(f"diff_25 : {diff_25}\n")

symm_diff_25 = set2.symmetric_difference(set5)
print(f"symm_diff_25 : {symm_diff_25}\n")

# subset superset
sub_52 = set5.issubset(set2)
print(f"sub_52 : {sub_52}\n")

super_25 = set2.issuperset(set5)
print(f"super_25 : {super_25}\n")

# equal
equal_25 = set2 == set5
print(f"equal_25 : {equal_25}\n")


tinydict = {"a" : 1, "b" : 2, "c" : 3}
a_val = tinydict["a"]
print(f"a_val : {a_val}")

tinydict["d"] = 5
print("tinydict", tinydict)

del(tinydict["a"])
print("tinydict", tinydict)


tinydict.clear()
print("tinydict", tinydict)

#tinydict2 = {["a"] : 1}


str1: str = "aabbcc"
str1: list = list(str1)
print("str: ", str1)


# Use join method need container inside all be string
list1 = ["1", "2", "3"]
tuple1 = (1, 2, 3, 4, 5)
list1_join = "_".join(list1)
print(list1_join)

data = {3: "apple", 1: "banana", 2: "cherry"}
result = sorted(data)
print(result)  # Output: [1, 2, 3]

dict1 = {"apple": 1, "banana": 3, "orange": 2}
dict1_sorted = sorted(dict1.items(), key=lambda x: x[1])
print(dict1_sorted)


str2 = "abc" \
    "def"

print(str2)

str3 = "   I am a person."
print(str3.split())

print(str3.strip())

str4 = "Hello"
print("{} {} {} {} {}".format(*str4))


a = [1, 2, 3]
b = [4, 5, 6]
zipped = zip(a, b)
a1, b1 = list(zip(*zipped)) # * =>uppacked (1, 4) (2, 5) (3, 6) zip => (1, 2, 3) (4, 5, 6)
print()


print(type(str(a)))





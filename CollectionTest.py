list1 = list()

print(list1)

list1 = [1,2,3]

print(list1)

print(list1[0])
print(list1[1])


print(list1[-2])

list2 = [1,2,["a","b"],3,4]

print(list2[2][0])

list2.append("a")

list2.reverse()

print(list2)

list2.remove(1)

print(list2)

del list2[0]

print(list2)

for index,item in enumerate(list2,3):
    print(index,": ",item)
    
    
list3 = list2[1:4:2]

print(list3)

list4 = list2[4:1:-1]

print(list4)


la1 = [1,2]

la2 = [2,3]

lc3 = la1+ la2

print(lc3)

la1_m = la1 * 3

print(la1_m)

set1 = {1,2,3}
set2 = {2,3,4}
set3 = set1.union(set2)

print("set3=",set3)

union_set = set1 | set2

print("union_set=",union_set)

intersection_set = set1 & set2

print("intersection_set=",intersection_set)


diff_set = set1 - set2

print("diff_set=",diff_set)


# 对称差集,互相没有的元素
symmetry_set = set1 ^ set2

print("symmetry_set=",symmetry_set)


d1 = {"name":"xiaoqi","age":10,"gender":"B"}

print(d1)

print(d1.get("name"))

d1["job"] = "合欢"

print(d1)

print(d1.pop("job"))

print(d1)

for di in d1.items():
    print("d1 for=", di)
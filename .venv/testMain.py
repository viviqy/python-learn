import sys

print("hello 1")
print("1", 2, 3, "4", 5.5)

age = 18

gender = "girl"

print(gender, age)

print(1 == 1, 1 != 1)

try:
    1 / 0;
except:
    print("error 0")

print(type("11"))
print(type(11))
print(type(1.111111111111111111111111111))
print(type("2020-11-11"))

may_max = 999 ** 9
sys.set_int_max_str_digits(0)
print(may_max)

print(3.3e+2)

text1 = "aaaa"
text2 = """aaaaa
    bbbbb
    ccccc"""

print(text1)
print(text2)

pageNum = 1
pageSize = 1
totalRecords = 10

format_text = f"pageNum={pageNum},pageSize={pageSize},totalRecords={totalRecords}"
print(format_text)
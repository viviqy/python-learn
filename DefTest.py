def sayHi():
    print("hi")


sayHi()


def sayWord(word):
    print(word)


sayWord("hehe")


def add1(number):
    return int(number + 1);


print(add1(1))

money = None

print(money)

CONST_A = 1


def testGlobal():
    global CONST_A
    CONST_A +=1
    print(CONST_A)

testGlobal()
print(CONST_A)
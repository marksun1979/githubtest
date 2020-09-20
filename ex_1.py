# 1、（a）
theProduct = 10
for i in range(1,30):
    print("i=",i)
    print("Running total = ",theProduct)
    if i%3==0:
        theProduct *=i
print(theProduct)
""""
i= 1
Running total =  10
i= 2
Running total =  10
i= 3
Running total =  10
i= 4
Running total =  30
i= 5
Running total =  30
i= 6
Running total =  30
i= 7
Running total =  180
i= 8
Running total =  180
i= 9
Running total =  180
i= 10
Running total =  1620
i= 11
Running total =  1620
i= 12
Running total =  1620
i= 13
Running total =  19440
i= 14
Running total =  19440
i= 15
Running total =  19440
i= 16
Running total =  291600
i= 17
Running total =  291600
i= 18
Running total =  291600
i= 19
Running total =  5248800
i= 20
Running total =  5248800
i= 21
Running total =  5248800
i= 22
Running total =  110224800
i= 23
Running total =  110224800
i= 24
Running total =  110224800
i= 25
Running total =  2645395200
i= 26
Running total =  2645395200
i= 27
Running total =  2645395200
i= 28
Running total =  71425670400
i= 29
Running total =  71425670400
71425670400
"""
# 1、（b）
l1=[1,2,3]
l2=[1,2,3,4]
l3=[1,2,3,4,5]
def lOrder(l1,l2,l3):
    if len(l1)<len(l2)<len(l3):
        return True
    else:
        return False
print(lOrder(l1,l2,l3))
if lOrder(l1,l2,l3):
    print("len(l1)<len(l2) <len(l3)是真的")
else:
    print("len(l1)<len(l2) <len(l3)是假的")
"""
True
len(l1)<len(l2) <len(l3)是真的
"""
# 1、（c）
str="123456"
def substrT(str):
    return str[len(str)-3:]
print(substrT(str))
"""
456
"""
# 1、（d）
list01=["a","b","c","d"]

def pinjie(list):
    str=""
    for item in list:
        str+=item
    return str
catString=pinjie(list01)
print(catString)
"""
abcd
"""
# 1、（e）
dic01={"1":1,"2":2,"3":3,"4":3}
def getList(dic):
    list01=[]
    for key in dic01:
        list01.append(key)
    return list01
print(getList(dic01))
"""
['1', '2', '3', '4']
"""
# 1、（f）
# RuntimeError: dictionary changed size during iteration!!!!!!
# 由于字典在迭代的时候不能变化长度所以要遍历列表，
# 以列表的内容判断字典的keys集合
ages = {"N":1 ,"R":2 ,"W":0 ,"J":4 ,"H":1}
S=['N','R']
for key in S:
    if key in ages.keys():
        del(ages[key])
print(ages)
"""
{'W': 0, 'J': 4, 'H': 1}
"""
# 2、（a）
myString ="01234567"
for i in range(len(myString)):
    if i<len(myString)/2:
        print(myString[i:i+3:2])
"""
02
13
24
35
"""
i=0
while i<len(myString)/2:
    print(myString[i:i + 3:2])
    i+=1
"""
02
13
24
35
"""
j=0
for i in range(len(myString)):
    if i<len(myString)/2:
        print(myString[i:i+3:2])
    else:
        print("STOP")
        j=1
print(j)
"""
STOP
STOP
STOP
STOP
1
"""
# 2、（b）
k=["milk","eggs","bread","cheese","jam"]
v=[1,12,2,5,2]
def f(keys,vals):
    d={}
    for i in range(len(keys)):
        d[keys[i]]=vals[i]
    return d
D1=f(k,v)
# print(D1["yoghurt"])
"""
'yoghurt'根本没有这个key 所以报错啊
"""
# 2、ii
# 没有什么不一样的，字典是无序的
# 2、iii
def f(keys,vals):
    list01=[]
    for i in range(len(k)):
        list01.append((k[i],v[i]))
    return list01
print(f(k,v))
"""
[('milk', 1), ('eggs', 12), ('bread', 2), ('cheese', 5), ('jam', 2)]
"""
# 3、（a）
def histogram(str):
    dic={}
    for item in str:
        if item in dic.keys():
            dic[item]+=1
        else:
            dic[item]=1
    return dic
print(histogram("parrot"))
"""
{'p': 1, 'a': 1, 'r': 2, 'o': 1, 't': 1}
"""
# 3、（b）
def filter_even(tuple_t):
    tuple01=()
    list01=[]
    for i in range(1,len(tuple_t),2):
        list01.append(tuple_t[i])
    tuple01=tuple(list01)
    return tuple01
print(filter_even((1,2,3,4,5,6,7,8,9,10)))
"""
[2, 4, 6, 8, 10]
"""
# 3、（c）
def reverse(list):
    return list[::-1]
print(reverse([0,1,2]))
"""
[2, 1, 0]
"""
# 4、（a）
# 没看明白
# 4、（b）
# 递归方法
def Fn(f,g,n):
    if n==0:
        return (0)
    elif n==1:
        return (1)
    return (f(f,g,n-1)+g(f,g,n-2))
for i in range(1,10):
    print(Fn(Fn,Fn,i))
"""
1
1
2
3
5
8
13
21
34
"""

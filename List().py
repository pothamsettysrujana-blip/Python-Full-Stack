Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#List[]
a[4,5.3,"python",5+3j,True,False]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a[4,5.3,"python",5+3j,True,False]
NameError: name 'a' is not defined
a=[4,5.3,"python",5+3j,True,False]
print(a)
[4, 5.3, 'python', (5+3j), True, False]
type(a)
<class 'list'>
b=3
type(b)
<class 'int'>
c=[3]
type(c)
<class 'list'>
a=["python","java","ai"]
a
['python', 'java', 'ai']
a.append("c")
a
['python', 'java', 'ai', 'c']
a.append("c","c++")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.append("c","c++")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["c","c++"])
a
['python', 'java', 'ai', 'c', ['c', 'c++']]
#extend
a=["ai","ml","ds"]
a.extend(["c","c++","python"])
a
['ai', 'ml', 'ds', 'c', 'c++', 'python']
#insert
b=["vij","hyd"]
b.insert(1,"vzg")
b
['vij', 'vzg', 'hyd']
#index
a=["black","white","red","green"]
a.index("green")
3
#copy
a.copy()
['black', 'white', 'red', 'green']
b=a.copy()
#count
b.count("black")
1
#sort()

a=["grapes","mango","apple","orange"]
a.sort()
a
['apple', 'grapes', 'mango', 'orange']
b=[5,7,2,4,0,33,22,15,37]
b.sort()
b
[0, 2, 4, 5, 7, 15, 22, 33, 37]
>>> #reverse()
>>> a=[34,75,14,47,65,80]
>>> a.reverse()
>>> a
[80, 65, 47, 14, 75, 34]
>>> b=["css","java","html"]
>>> b.reverse()
>>> b
['html', 'java', 'css']
>>> #pop()
>>> a=["c","c++","ml","ai"]
>>> a.pop()
'ai'
>>> a
['c', 'c++', 'ml']
>>> a.pop("c")
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.pop("c")
TypeError: 'str' object cannot be interpreted as an integer
>>> a.pop(1)
'c++'
>>> a
['c', 'ml']
>>> #remove()
>>> a.remove("ml")
>>> a
['c']
>>> a=["viji","suni","yashu","suji"]
>>> len(a)
4
>>> b=["suji"]
>>> len(b)
1
>>> b="suji"
>>> len(b)
4
>>> #clear()
>>> a.clear()
>>> a
[]
>>> b=[]
>>> b.append("hi")
>>> b
['hi']

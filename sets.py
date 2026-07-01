Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #sets
>>> a={4,5.3,"python",5+3j,True,False}
>>> print(a)
{False, True, 4, 5.3, 'python', (5+3j)}
>>> type(a)
<class 'set'>
>>> #subset
>>> a={3,5,6,7,9}
>>> b={5,6,7}
>>> b.issubset(a)
True
>>> a.issubset(b)
False
>>> #superset
>>> a.issuperset(b)
True
>>> b.issuperset(a)
False
>>> #union
>>> a={3,5,4,7,8,10}
>>> b={1,2,6,4,9,3,4}
>>> a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> c={6,4,,7,9,11}
SyntaxError: invalid syntax
>>> c={6,4,5,7,9,11}
>>> c
{4, 5, 6, 7, 9, 11}
>>> #intersection()
>>> a={3,5,4,6,7,9}
>>> b={2,4,6,8,9,5}
>>> a.intersection(b)
{9, 4, 5, 6}
>>> #update()
>>> a={10,20,30,40,50}
>>> b={30,40,50,60,70}
>>> a
{50, 20, 40, 10, 30}
>>> a.update(b)
>>> a
{70, 40, 10, 50, 20, 60, 30}
>>> b
{50, 70, 40, 60, 30}
>>> a.update(b)
a
{70, 40, 10, 50, 20, 60, 30}
b.update(a)
b
{70, 40, 10, 50, 20, 60, 30}
#difference()
a={2,4,5,12,15,17,20,32,34}
b={3,5,7,8,9,11,16,20,32,35}
a.difference(b)
{2, 34, 4, 12, 15, 17}
b.difference(a)
{35, 3, 7, 8, 9, 11, 16}
#symmetric difference
a={2,4,5,12,15,17,20,32,34}
b={2,5,8,9,12,16,20,32,35}
a.symmetric_difference(b)
{34, 35, 4, 8, 9, 15, 16, 17}
#intesection update
a={3,5,4,6,7,9}
b={2,4,6,8,9,5}
a.intersection_update(b)
a
{9, 4, 5, 6}
b.intersection_update(a)
b
{9, 4, 5, 6}
b
{9, 4, 5, 6}
a={3,5,4,6,7,9}
b={2,4,6,8,9,5}
a.difference_update(b)
a
{3, 7}
b.difference_update(a)
b
{2, 4, 5, 6, 8, 9}
#symmetric differece update
a={2,4,5,12,15,17,20,32,34}
b={2,5,8,9,12,16,20,32,35}
a.symmetric_difference_update(b)
a
{34, 4, 35, 8, 9, 15, 16, 17}
b.symmetric_difference_update(a)
b
{32, 2, 34, 5, 4, 12, 15, 17, 20}
#pop()
a={3,4,5,6,7,8,9}
a.pop()
3
a.pop(6)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a.pop(6)
TypeError: set.pop() takes no arguments (1 given)
a.remove(6)
a
{4, 5, 7, 8, 9}
#discard
a={3,4,5,6,7,8,9}
a.discard(6)
#copy
a.copy()
{3, 4, 5, 7, 8, 9}
a
{3, 4, 5, 7, 8, 9}
#clear
a.clear()
a
set()
#add
b=set()
b.add(3)
b
{3}
#count and index
a={4,5,6,7}
len(a)
4
a.count
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    a.count
AttributeError: 'set' object has no attribute 'count'
a.index
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    a.index
AttributeError: 'set' object has no attribute 'index'

#isdisjoint
a={3,4,5,6,7}
b={8,9,10,11}
a.isdisjoint(b)
True

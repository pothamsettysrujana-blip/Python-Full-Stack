Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=2,b=5
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=2;b=5
print(a+b)
7
a,b=2,4
print(a+b)
6
a,b,c=10
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a,b,c=10
TypeError: cannot unpack non-iterable int object
>>> a=b=c=10
>>> print(a,b,c)
10 10 10
>>> a,b,c=12,4,9
>>> print(a,b,c)
12 4 9
>>> a,b,c=3,5,6,7,2
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a,b,c=3,5,6,7,2
ValueError: too many values to unpack (expected 3, got 5)
>>> a,b,c=(3,5,6)
>>> print(a,b,c)
3 5 6
>>> first name="srujana"
SyntaxError: invalid syntax
>>> first_name="srjana"
>>> firstname="srujana"
>>> print(first_name)
srjana
>>> print(firstname)
srujana
>>> fname="srujana"
>>> lname="p"
>>> print(fname+lname)
srujanap
>>> print(fname+" "+lname)
srujana p
>>> print(fname,lname)
srujana p
>>> name="srujana"
>>> print(name)
srujana
>>> NAME="srujana"
>>> print(NAME)
srujana
>>> Name="srujana"
>>> print(Name)
srujana
>>> a=3
>>> print(a)
3
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined

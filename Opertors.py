Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # Operators
>>> # Arithematic Operator
>>> a=5
>>> b=3
>>> print(a+b)
8
>>> print(a-b)
2
>>> print(a*b)
15
>>> print(a//b)
1
>>> print(a/b)
1.6666666666666667
>>> print(a**b)
125
>>> print(a%b)
2
>>> # Assignment Operator
>>> a=4
>>> b=5
>>> print(a+=b)
SyntaxError: invalid syntax
>>> a+b
9
>>> b+=a
>>> b
9
>>> print(b)
9
>>> b-=3
>>> b
6
>>> b*=3
>>> b
18
>>> b//=2
>>> b
9
>>> b/=2
>>> b
4.5
>>> b**=4
>>> b
410.0625
>>> b%=3
>>> b
2.0625
# Comparision Operator
a=3
b=4
a
3
a<b
True
a>b
False
b<a
False
b>a
True
a!=b
True
a==b
False
a<=b
True
a>=b
False
b<=a
False
b>=a
True
a=3
b=3
a==b
True
# Logical Operator
a=5
d=9
a<b and b>a
False
a<=b and b>=a
False
a!=b and a==b
False
a<b or b>a
False
a<d and d>a
True
a<=b and b>=a
False
a<=d and d>=a
True
not True
False
not False
True
# Identify
a=4
type(a) is int
True
type(a) is not int
False
b=5.7
type(b) is float
True
type(b) is not float
False
type(b) is str
False
c='sujana'
type(c) is str
True
type(c) is not str
False
d=5+7j
type(d) is complex
True
type(d) is not complex
False
e=True
type(e) is bool
True
type(e) is not bool
False
# membership
a=2,3,4,5,6,1
4 in a
True
9 in a
False

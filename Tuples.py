Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Tuple
>>> a=(4,5.3,"python",5+3j,True,False)
>>> print(a)
(4, 5.3, 'python', (5+3j), True, False)
>>> type(a)
<class 'tuple'>
>>> #count()
>>> a.count(5+3j)
1
>>> #index()
>>> a.index(True)
4
>>> len(a)
6

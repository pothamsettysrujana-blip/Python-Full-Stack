Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dist{}
a={"name":"srujana","city":"vij"}
print(a)
{'name': 'srujana', 'city': 'vij'}
type(a)
<class 'dict'>
b={2,3,4,"suji"}
type(b)
<class 'set'>
#Types of dict{}
a={"name":"srujana","mailid":"srjana@gmail.com","mobile.no":"324686268"}
print(a)
{'name': 'srujana', 'mailid': 'srjana@gmail.com', 'mobile.no': '324686268'}
a.keys()
dict_keys(['name', 'mailid', 'mobile.no'])
a.values()
dict_values(['srujana', 'srjana@gmail.com', '324686268'])
a.items()
dict_items([('name', 'srujana'), ('mailid', 'srjana@gmail.com'), ('mobile.no', '324686268')])
>>> #update
>>> a={"course":"python","institute":"codegnan"}
>>> a.update({"name":"srujana"})
>>> a
{'course': 'python', 'institute': 'codegnan', 'name': 'srujana'}
>>> a.update({"year":2026},{"month":7})
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.update({"year":2026},{"month":7})
TypeError: update expected at most 1 argument, got 2
>>> a.update({"year":2026,"month":7})
>>> a
{'course': 'python', 'institute': 'codegnan', 'name': 'srujana', 'year': 2026, 'month': 7}
>>> #default()
>>> a={"year":2026,"month":"july"}
>>> a.setdefault("date",2)
2
>>> a
{'year': 2026, 'month': 'july', 'date': 2}
>>> #pop() and popitem()
>>> a={"time":12,"hour":1,"min":3}
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
>>> a.pop("time":12)
SyntaxError: invalid syntax
>>> a.pop("time")
12
>>> a
{'hour': 1, 'min': 3}
>>> a.popitem()
('min', 3)
>>> a
{'hour': 1}
>>> #get()
>>> a={"college":"srm","branch":"cse"}
>>> a.get("college")
'srm'
>>> a["branch"]
'cse'
>>> a.get("cse")
>>> a
{'college': 'srm', 'branch': 'cse'}
a["cse"]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a["cse"]
KeyError: 'cse'
a={"hour":12,"min":3,"sec":60}
a.copy()a
SyntaxError: invalid syntax
a.copy(a)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a.copy(a)
TypeError: dict.copy() takes no arguments (1 given)
a={"hour":12,"min":3,"sec":60}
a.copy()
{'hour': 12, 'min': 3, 'sec': 60}
a
{'hour': 12, 'min': 3, 'sec': 60}
a.clear()
a
{}
b={}
b.update{"name":"suji"}
SyntaxError: invalid syntax
b.update({"name":"suji"})
b
{'name': 'suji'}
a={'course': 'python', 'institute': 'codegnan', 'name': 'srujana'}
len(a)
3
a.count()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a.count()
AttributeError: 'dict' object has no attribute 'count'
a={"name":"srujana","city":"vij","name":"srujana"}
print(a)
{'name': 'srujana', 'city': 'vij'}
a={"name":"srujana","city":"vij","name":"aswini"}
print(a)
{'name': 'aswini', 'city': 'vij'}
a={"name1":"srujana","city":"vij","name2":"srujana"}
print(a)
{'name1': 'srujana', 'city': 'vij', 'name2': 'srujana'}
a={"idnos":[10,20,30],"names":["viju","suni","yashu"],"marks":[40,50,60]}
print(a)
{'idnos': [10, 20, 30], 'names': ['viju', 'suni', 'yashu'], 'marks': [40, 50, 60]}
type(a)
<class 'dict'>
a.keys()
dict_keys(['idnos', 'names', 'marks'])
a.values()
dict_values([[10, 20, 30], ['viju', 'suni', 'yashu'], [40, 50, 60]])
a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['viju', 'suni', 'yashu']), ('marks', [40, 50, 60])])

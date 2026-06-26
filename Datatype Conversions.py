Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Datatype Conversions
>>> #int
>>> int(4)
4
>>> int(5.9)
5
>>> int('code')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int('code')
ValueError: invalid literal for int() with base 10: 'code'
>>> int(4+6j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(4+6j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(True)
1
>>> int(False)
0
>>> #Float
>>> float(4)
4.0
>>> float(3.6)
3.6
>>> float('srujana')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float('srujana')
ValueError: could not convert string to float: 'srujana'
>>> float(3+9j)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(3+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float(True)
1.0
>>> float(False)
0.0
>>> #String
>>> str(4)
'4'
>>> str(1.6)
'1.6'
>>> str("codengnan")
'codengnan'
>>> str(3+6j)
'(3+6j)'
str(True)
'True'
str(False)
'False'
#Complex
complex(6)
(6+0j)
complex(9.4)
(9.4+0j)
complex('python')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    complex('python')
ValueError: complex() arg is a malformed string
complex(5+24j)
(5+24j)
complex(True)
(1+0j)
cmplex(False)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    cmplex(False)
NameError: name 'cmplex' is not defined. Did you mean: 'complex'?
complex(False)
0j
#Boolen
bool(5)
True
boo(2.5)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    boo(2.5)
NameError: name 'boo' is not defined. Did you mean: 'bool'?
bool(0.5)
True
bool('code')
True
bool(4+5j)
True
bool(True)
True
bool(False)
False

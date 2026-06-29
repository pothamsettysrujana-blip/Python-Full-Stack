Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Slicing
>>> a="codegnan"
>>> a[0:3]
'cod'
>>> a[0:4]
'code'
>>> a[4:8]
'gnan'
>>> a[:4]
'code'
>>> a[4:]
'gnan'
>>> b="work until you succeed"
>>> b[5:10]
'until'
>>> b[11:14]
'you'
>>> b[:4]
'work'
>>> b[15:20]
'succe'
>>> b[15:21]
'succee'
>>> b[15:22]
'succeed'
>>> c="codegnan it solutions"
>>> c[9:11]
'it'
>>> b[:8]
'work unt'
>>> b[0:8]
'work unt'
>>> c="codegnan it solutions"
>>> c[9:11]
'it'
>>> c[0:8]
'codegnan'
>>> c[12:21]
'solutions'
>>> #negitive
>>> d="vijayawada is a  royal city"
>>> d[-10:-6]
'roya'
>>> d[-10:-6]
... 'roya'
SyntaxError: multiple statements found while compiling a single statement
>>> d[-10:-5]
'royal'
d[-4:]
'city'
d[-26:-16]
'ijayawada '
d[-27:-16]
'vijayawada '
e="vizag is city of destiny"
e[-15:-11]
'city'
e[-24:-19]
'vizag'
e[-7:]
'destiny'

Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # Indexing
>>> # Positive Indexing
>>> a= "I am in class"
>>> a[3]
'm'
>>> a[7]
' '
>>> a[5]
'i'
>>> a[8]+a[9]+a[10]+a[11]+a[12]
'class'
>>> a[2]+a[3]
'am'
>>> a[1]+a[4]+a[7]
'   '
>>> b="I am learing python course"
>>> b[14]+b[15]+b[16]+b[17]+b[18]+b[19]
'ython '
>>> b="I am learning python course"
>>> b[14]+b[15]+b[16]+b[17]+b[18]+b[19]
'python'
>>> b[5]+b[6]+b[7]+b[8]+b[8]+b[9]+b[10]+b[11]+b[12]
'learrning'
>>> b[21]+b[22]+b[23]+b[24]+b[25]+b[26]
'course'
>>> c="Time is very precious"
>>> c[13]+[14]+c[15]+c[16]+c[17]+c[18]+c[19]+c[20]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    c[13]+[14]+c[15]+c[16]+c[17]+c[18]+c[19]+c[20]
TypeError: can only concatenate str (not "list") to str
>>> d= "time is very precious"
>>> d[13]+d[14]+d[15]+d[16]+d[17]+d[18]+d[19]+d[20]
'precious'
>>> d[8]+d[9]+d[10]+d[11]
'very'
>>> d[0]+d[1]+d[2]+d[3]
'time'
>>> # Negitive indexing
>>> a="Simple is better than complex"
>>> a[-29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
'Simple'
>>> a[-12]+a[-11]+a[-10]+a[-9]
'than'
>>> a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+c[-1]
'comples'
>>> a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'complex'
a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
'better'
b="I love python"
b[-11]+b[-10]+b[-9]+b[-8]
'love'

b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'python'

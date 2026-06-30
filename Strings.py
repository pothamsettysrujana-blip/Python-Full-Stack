Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # Strings
>>> # len()
>>> a="pyhton"
>>> len(a)
6
>>> b="python course"
>>> len(b)
13
>>> c=""
>>> len(c)
0
>>> d=" "
>>> len(d)
1
>>> # count()
>>> a="twinkle twinkle little star"
>>> count(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> a.count("twinkle")
2
>>> a.count("t")
5
>>> a.count("i")
3
>>> a.count(" ")
3
>>> a.count("w")
2
>>> # find a string
>>> a="code"
>>> a.find("d")
2
>>> a.find("c")
0
>>> b="hello"
>>> a.find("l")
-1
>>> b.find("l")
2
>>> # escape sequences
>>> #\n->new line
#\t->tab space
a="nname\nmobile\temailid\nclg"
print(a)
nname
mobile	emailid
clg
a="name:srujana\nmobile:468496461\temailid:srujana@gmail.com\nclg:SRM"
print(a)
name:srujana
mobile:468496461	emailid:srujana@gmail.com
clg:SRM
# replace
a="wait until you succeed"
a.replace("wwait","work")
'wait until you succeed'
a.replace("wait","work")
'work until you succeed'
b="wait wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b.replace("wait","work")
'work work until you succeed'
b.replace("wait","work",1)
'work wait until you succeed'
#upper()
a="hello"
a.upper()
'HELLO'
#lowe()
#lower()
b="CODE"
b.lower()
'code'
#captalize()
c="python"
c.captalize()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    c.captalize()
AttributeError: 'str' object has no attribute 'captalize'. Did you mean: 'capitalize'?
c.capitalize
<built-in method capitalize of str object at 0x000001DC1526BEA0>
d="python"
d.capitalize()
'Python'

a="python course"
a.title()
'Python Course'
b="i am in class"
a.title()
'Python Course'
b.title()
'I Am In Class'
#true and flase
#true and false
a="java"
a.isupper()
False
a.islower()
True
a.isdigit()
False
a.isalpha()
True
b="python course"
b.isalpha()
False
c="pythoncourse"
c.isalpha()
True
d="1234"
d.isdigit()
True
d.isalnum()
True
e="suji123"
e.isalnum()
True
e="suji@123"
e.isalnum()
False

a="hello python"
a.startwith("h")
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a.startwith("h")
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
a.startswith("h")
True
a.endwith("n")
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    a.endwith("n")
AttributeError: 'str' object has no attribute 'endwith'. Did you mean: 'endswith'?
a.endswith("n")
True

#strip()
#lstrip(), rstrip()
a="      code      "
+
a.strip()
'code'
a.lstrip()
'code      '
a.rstrip()
'      code'

#split()
a="python c c++ java"
a.split()
['python', 'c', 'c++', 'java']
b="i am in vij"
b.split()
['i', 'am', 'in', 'vij']
c="code"
c.split()
['code']

#join()
a="vij hyd vzg"
"".join()
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    "".join()
TypeError: str.join() takes exactly one argument (0 given)
"".join(a)
'vij hyd vzg'
b="vij","hyb","vzg"
"".join(b)
'vijhybvzg'
" ".join(b)
'vij hyb vzg'
"f".join(b)
'vijfhybfvzg'

#
a="hello"
b="world"
print(a+b)
helloworld
print(a+" "+b)
hello world
fname="srujana"
lname="p"
print(fname+lname)
srujanap
print(fname+" "+lname)
srujana p
print(fname.title()+" "+lname.title())
Srujana P
print((fname+" "+lname).title())
Srujana P

#formatting
a=3
b=9
print(a+b)
12
print("the sum is",a+b)
the sum is 12
x="vij"
print("city is",x)
city is vij

#.format method
a="mottu"
="patlu"
SyntaxError: invalid syntax
b="patlu"
print("hello",a+b)
hello mottupatlu
print("hello {}{}".format(a,b))
hello mottupatlu
print("hello {} {}".format(a,b))
hello mottu patlu
print("hello {} hello{}".format(a,b))
hello mottu hellopatlu

#fstring
a="sita"
b="ram"
print(f"hello {a}{b}")
hello sitaram
print(f"hello {a} {b}")
hello sita ram

print(f"hello {a}hello {b}")
hello sitahello ram
print(f"hello {a} hello {b}")
hello sita hello ram

a=5
b=3
print(f"the product of {}{}".format(a*b))
SyntaxError: f-string: valid expression required before '}'
print(f"the product of ".format(a*b))
the product of 
print(f"the product of".a*b)
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    print(f"the product of".a*b)
AttributeError: 'str' object has no attribute 'a'
a=4
b=5

===================================================================== RESTART: Shell ====================================================================
a=6
b=2
c=a*b
print("the product is{}".format())
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    print("the product is{}".format())
IndexError: Replacement index 0 out of range for positional args tuple
print("the product is{}".format(c))
the product is12
print(f"the product is{c})
      
SyntaxError: unterminated f-string literal (detected at line 1)
print(f"the product is{c}")
      
the product is12
print("the product is{}".format(a*b))
      
the product is12
print(f"the product is{a*b}"))
SyntaxError: unmatched ')'
print(f"the product is{a*b}")
the product is12

#CONDITIONS
#if-conditions by using comparision operators
#<,>,<=,>=,!=,==
'''a=10
b=20
if a<b:
    print("true")'''

'''a=10
b=20
if a>b:
    print("true")'''

'''a=5
b=7
if a<=b:
    print("less")'''

'''a=10
b=20
if a>=b:
    print("true")'''

'''a=10
b=10
if a==b:
    print("true")'''

'''a=10
b=20
if a!=b:
    print("true")'''

'''a="python"
if a=="python":
    print("match")'''
    
'''a=int(input("a value"))
b=int(input("b value"))
if a<b:
    print("less")'''

'''a=int(input("a value"))
if a<50:
    print("less")'''

#using run-time
'''a=int(input("value of a:"))
b=int(input("value of b:"))
if a<b:
    print("true")'''


'''a=int(input("value of a:"))
b=int(input("value of b:"))
if a>b:
    print("true")'''

'''a=int(input("value of a:"))
b=int(input("value of b:"))
if a<=b:
    print("less")'''

'''a=int(input("value of a:"))
b=int(input("value of b:"))
if a>=b:
    print("true")'''

'''a=int(input("value of a:"))
b=int(input("value of b:"))
if a==b:
    print("true")'''

'''a=int(input("value of a:"))
b=int(input("value of b:"))
if a!=b:
    print("true")'''

'''a=input("value of a:")
if a=="python":
    print("match")'''




#if-conditions by using logical operators
#and,or,not
'''a=3
b=6
if a<b and b>a:
    print("true")'''

'''a=4
b=7
if a<=b and b>=a:
    print("true")'''

'''a=9
b=12
if a!=b and a==b:
    print("true")'''

'''a=2
b=6
if a<b or b>a:
    print("true")'''

'''a=3
b=6
if a!=b or a==b:
    print("true")'''

'''a=5
b=7
if not a<b:
    print("true") '''

'''a=3
b=6
if not a>b:
    print("true")'''

'''a=3
b=6
if not a<b and b>a:
    print("true")'''

'''a=3
b=6
if a<b or b>a:
    print("true")'''
#using run-time
'''a=int(input("value of a:"))
b=int(input("value of b:"))
if a<b and b>a:
    print("true")'''

'''a=int(input("value of a:"))
b=int(input("value of b:"))
if a<=b and b>=a:
    print("true")'''

'''a=int(input("value of a:"))
b=int(input("value of b:"))
if a!=b and a==b:
    print("true")'''

'''a=int(input("value of a:"))
b=int(input("value of b:"))
if a<b or b>a:
    print("true")'''

'''a=int(input("value of a:"))
b=int(input("value of b:"))
if a!=b or a==b:
    print("true")'''

'''a=int(input("value of a:"))
b=int(input("value of b:"))
if not a<b:
    print("true")'''

'''a=int(input("value of a:"))
b=int(input("value of b:"))
if not a>b:
    print("true")'''

'''a=int(input("value of a:"))
b=int(input("value of b:"))
if not a<b and b>a:
    print("true")'''

'''a=int(input("value of a:"))
b=int(input("value of b:"))
if not a<b or b>a:
    print("true")'''


#if-conditions by using identify operators
#is, is not
'''a=3
if type(a) is int:
    print("is int")'''

'''a=3
if type(a) is not int:
    print("is int")'''

'''a=5.3
if type(a) is float:
    print("is float")'''

'''a=5.3
if type(a) is not float:
    print("is float")'''

'''a="srujana"
if type(a) is str:
    print("is string")'''

'''a="srujana"
if type(a) is str:
    print("is not string")'''

'''a=2+4j
if type(a) is complex:
    print("is complex")'''

'''a=2+4j
if type(a) is not complex:
    print("is complex")'''

'''a=True
if type(a) is bool:
    print("is boolean")'''

'''a=True
if type(a) is not bool:
    print("is boolean")'''
#using run-time 
'''a=int(input("value: "))
if type(a) is int:
    print("is integer")'''


'''a=float(input("value: "))
if type(a) is float:
    print("is float")'''

'''a=str(input("value: "))
if type(a) is str:
    print("is string")'''

'''a=complex(input("value: "))
if type(a) is complex:
    print("is complex")'''

'''a=bool(input("value: "))
if type(a) is bool:
    print("is boolean")'''

    
#if-conditions by using membership operators
'''a=2,3,4,5,6,7,8
if 8 in a:
    print("true")'''

'''a=2,3,4,5,6,7,8
if 20 not in a:
    print("true")'''

'''a=int(input())
if 30 in a:
    print("true")'''#error

'''a=int(input("value"))
b=2,3,4,5,6,10
if a in b:
    print("true")'''

#IF-ELSE
#if-else conditions by using comparision operators
'''a=4
b=8
if a<b:
    print("less")
else:
    print("false")'''

'''a=4
b=8
if a>b:
    print("less")
else:
    print("false")'''

'''a=5
b=7
if a<=b:
    print("less")
else:
    print("false")'''


'''a=10
b=20
if a>=b:
    print("true")
else:
    print("false")'''


'''a=10
b=10
if a==b:
    print("true")
else:
    print("false")'''

'''a=10
b=10
if a!=b:
    print("true")
else:
    print("false")'''

#if-else conditions by using logical operators
#and,or,not
'''a=3
b=6
if a<b and b>a:
    print("true")
else:
    print("false")'''


'''a=4
b=7
if a<=b and b>=a:
    print("true")
else:
    print("false")'''

'''a=9
b=12
if a!=b and a==b:
    print("true")
else:
    print("false")'''

'''a=2
b=6
if a<b or b>a:
    print("true")
else:
    print("false")'''

'''a=3
b=6
if a!=b or a==b:
    print("true")
else:
    print("false")'''

'''a=5
b=7
if not a<b:
    print("true")
else:
    print("false")'''

'''a=3
b=6
if not a>b:
    print("true")
else:
    print("false")'''

'''a=3
b=6
if not a<b and b>a:
    print("true")
else:
    print("false")'''

'''a=3
b=6
if a<b or b>a:
    print("true")
else:
    print("false")'''
#using run-time
'''a=int(input("value of a:"))
b=int(input("value of b:"))
if a<b and b>a:
    print("true")
else:
    print("false")'''

'''a=int(input("value of a:"))
b=int(input("value of b:"))
if a<=b and b>=a:
    print("true")
else:
    print("false")'''

'''a=int(input("value of a:"))
b=int(input("value of b:"))
if a!=b and a==b:
    print("true")
else:
    print("false")'''

'''a=int(input("value of a:"))
b=int(input("value of b:"))
if a<b or b>a:
    print("true")
else:
    print("false")'''

'''a=int(input("value of a:"))
b=int(input("value of b:"))
if a!=b or a==b:
    print("true")
else:
    print("false")'''

'''a=int(input("value of a:"))
b=int(input("value of b:"))
if not a<b:
    print("true")
else:
    print("false")'''

'''a=int(input("value of a:"))
b=int(input("value of b:"))
if not a>b:
    print("true")
else:
    print("false")'''

'''a=int(input("value of a:"))
b=int(input("value of b:"))
if not a<b and b>a:
    print("true")
else:
    print("false")'''

'''a=int(input("value of a:"))
b=int(input("value of b:"))
if not a<b or b>a:
    print("true")
else:
    print("false")'''


#if-else conditions by using identify operators
#is, is not
'''a=3
if type(a) is int:
    print("is int")
else:
    print("is not int")'''

'''a=3
if type(a) is not int:
    print("is int")
else:
    print("is not int")'''

'''a=5.3
if type(a) is float:
    print("is float")
else:
    print("is not int")'''

'''a=5.3
if type(a) is not float:
    print("is float")
else:
    print("is not int")'''

'''a="srujana"
if type(a) is str:
    print("is string")
else:
    print("is not int")'''

'''a="srujana"
if type(a) is str:
    print("is not string")
else:
    print("is not int")'''

'''a=2+4j
if type(a) is complex:
    print("is complex")
else:
    print("is not int")'''

'''a=2+4j
if type(a) is not complex:
    print("is complex")
else:
    print("is not int")'''

'''a=True
if type(a) is bool:
    print("is boolean")
else:
    print("is not int")'''

'''a=True
if type(a) is not bool:
    print("is boolean")
else:
    print("is not int")'''
#using run-time 
'''a=int(input("value: "))
if type(a) is int:
    print("is integer")
else:
    print("is not int")'''


'''a=float(input("value: "))
if type(a) is float:
    print("is float")
else:
    print("is not int")'''

'''a=str(input("value: "))
if type(a) is str:
    print("is string")
else:
    print("is not int")'''

'''a=complex(input("value: "))
if type(a) is complex:
    print("is complex")
else:
    print("is not int")'''

'''a=bool(input("value: "))
if type(a) is bool:
    print("is boolean")
else:
    print("is not int")'''

#if-else conditions by using membership operators
'''a=2,3,4,5,6,7,8
if 8 in a:
    print("true")
else:
    print("False")'''

'''a=2,3,4,5,6,7,8
if 20 not in a:
    print("true")
else:
    print("False")'''

'''a=int(input())
if 30 in a:
    print("true")
else:
    print("False")'''#error

'''a=int(input("value"))
b=2,3,4,5,6,10
if a in b:
    print("true")
else:
    print("False")4'''


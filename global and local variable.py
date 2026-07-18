#global and local variable
#frist case of global variable
'''a=4
def check1():
    print("inside value is",a)
check1()
print("outside value is",a)'''

#second case of global variable
'''a=2
def check2():
    a=5
    a=a**2
    print("inside value is",a)
check2()
print("outside value is",a)'''

#third case of both global and local variable
'''a=6
def check3():
    a=8
    print("inside value is",a)
    a=10
    print("update value is",a+5)
    b=13#local variable
    b=b+a
    print("value of b is",b)
check3()
print("a value is",a)
print("b value is",b)'''

#usage global keyword
#when user wants to access the global var insdie the func directly and carry forward the updated value even outside the func then we need to use global keyword.
'''a=6
def final():
    global a,b
    print("inside the value is",a)
    a=15
    print("updted value is",a)
    b=20
    b=a+b
    print("value of b is",b)
final()
print("a value is",a)
print("b value is",b)'''

#task
#attendence tracker
'''students=int(input("enter number of students:"))
present=0
absent=0
for i in range(1,students+1):
    attendence=input(f"student {i} P/A:")
    if attendence=="present":
        p+=1
    elif attendence=="absent":
        a+=1
print("...attendence report...")
print("total students:",students)
print("no.of present:",present)
print("no.of absent:",absent)'''
    
    

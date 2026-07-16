#Funtions
'''a=10
b=20
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)
a=100
b=200
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)
a=1000
b=2000
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''

#def funtions
#sum,diff,product
'''def calculate(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

#div,pow,div
'''def calculate(a,b):
    print("the div is",a//b)
    print("the pow is",a**b)
    print("the mod is",a%b)
calculate(3,4)
calculate(12,16)
calculate(5,6)'''

'''def add(a,b):
    print(a+b)
add(4,9)'''

'''while True:
    def cal():
        a=int(input("a value:"))
        b=int(input("b value:"))
        print(a+b)
    cal()'''

'''def cal():
    a=int(input("a value:"))
    b=int(input("b value:"))
    print(a+b)
    cal()
cal()'''


'''def fullname():
    fname=input("first name:")
    lname=input("last name:")
    print((fname+" "+lname).title())
fullname()'''

#print and return
'''def mul(a,b):
    print(a*b)
mul()'''

'''def mul(a,b):
    return(a*b)
mul()'''

#print v/s return
'''def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
add(2,3)'''

'''def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return(c)
    #return(d)
    #return(e)
    return c,d,e
print(add(2,3))'''

#task1
#splitbill()
'''def splitbill():
    a=int(input("enter the bill"))
    b=int(input("no.of persons"))
    c=a//b
    print(c)
splitbill()'''

#using "fstring" and ".format"
'''def splitbill():
    a=int(input("enter the bill"))
    b=int(input("no.of persons"))
    c=a/b
    print(f"the split bill is {}".format(c))
    print(f"the split bill is {c}")
splitbill()'''


'''def splitbill():
    a=int(input("enter the bill"))
    b=int(input("no.of persons"))
    print("the split bill is {}".format(a//b))
    print(f"the split bill is {a//b}")
splitbill()'''

#task2
#add,sub,mul
'''while True:
    def cal():
        a=int(input("a value:"))
        b=int(input("b value:"))
        option=int(input("option 1.add 2.sub 3.mul"))
        if option==1:
            print(a+b)
        elif option==2:
            print(a-b)
        elif option==3:
            print(a*b)
    cal()'''

def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("a value:"))
    b=int(input("b value:"))
    option=int(input('''option
                        1.add
                        2.sub
                        3.mul'''))
    if option==1:
        add()
    elif option==2:
        sub()
    elif option==3:
        mul()

    





















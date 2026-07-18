#keyword and positional argument
'''def Details(id,name,emailid):
    id=10
    name="srujana"
    emailid="s@gmail.com"
    print(id,name,emailid)
Details(id="id",name="name",emailid="emailid")'''#step-1

'''def Details(id,name,emailid):
    print(id,name,emailid)
Details(id="id",name="name",emailid="emailid")
Details(id=20,name="vijitha",emailid="v@gmail.com")
Details(id=300,name="yashu",emailid="y@gmail.com") #step-2
Details(40,"sunitha","susu@gmail.com") #step-3
Details("vijitha","v@gmail.com",50) #step-4
Details(emailid="s@gmail.com",name="suji",id=50)'''#step5

#default argument
'''def grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f", % price)
grocery("sugar",100)'''

'''def grocery(item="rice",price=1600):
    print("item is %s" %item)
    print("price is %.2f", % price)
grocery()'''


'''def grocery(item,price=560):
    print("item is %s" %item)
    print("price is %.2f", % price)
grocery("dhal")'''

'''def grocery(item="ghee",price):
    #non def arg follows def args
    print("item is %s" %item)
    print("price is %.2f", % price)
grocery(360)'''#error


#task
'''def bakery(cake_name,price,qty):
    print("cake_name is %s" %cake_name)
    print("price is %.2f" %price)
    print("qty is %d kg/g" %qty)
bakery("black forest",900,2)'''

'''def bakery(cake_name="butter scotch",price=500,qty=1):
    print("cake_name is %s" %cake_name)
    print("price is %.2f" %price)
    print("qty is %d kg/g" %qty)
bakery()'''

'''def bakery(cake_name,price=1000,qty=3):
    print("cake_name is %s" %cake_name)
    print("price is %.2f" %price)
    print("qty is %d kg" %qty)
bakery("black current")'''

'''def bakery(cake_name="american nuts",price,qty):
    print("cake_name is %s" %cake_name)
    print("price is %.2f" %price)
    print("qty is %d kg/g" %qty)
bakery(900,2)'''


#star arguments
'''a=[2,3,4,5,6,7,8]
print(a)
print(*a)'''

'''a=(2,3,4,5,6,7,8)
print(a)
print(*a)'''


'''a={2,3,4,5,6,7,8}
print(a)
print(*a)'''

'''a=("name":"suji","city":"vij")
print(a)
print(*a)'''

'''c="python"
print(c)
print(*c)'''


'''a,b,c=1,2,3,4,5,6,7
print(a)
print(b)
print(c)'''#error

'''a,b,c=1,2,3
print(a)
print(b)
print(c)

*a,b,c=1,2,3,4,5,6,7
print(*a)
print(b)
print(c)

a,*b,c=1,2,3,4,5,6,7
print(a)
print(*b)
print(c)

a,b,*c=1,2,3,4,5,6,7
print(a)
print(b)
print(*c)

*a,b,*c=1,2,3,4,5,6,7
print(*a)
print(b)
print(*c)'''#error

'''a,b,c="codegnan"
print(a)
print(b)
print(c)'''#error

'''a,b,c="cod"
print(a)
print(b)
print(c)

*a,b,c="codegnan"
print(*a)
print(b)
print(c)

a,*b,c="codegnan"
print(a)
print(*b)
print(c)

a,b,*c="codegnan"
print(a)
print(b)
print(*c)'''

#Variable lengh arguments

'''def check(*a):
    print(a)
    print(type(a))
check()
check(1,2,3,4,5)
b=[3,4,5,6,7,8]
check(*b)
c={5,6,7,8,9}
check(*c)
d={"name":"srujana","age":21,"place":"vij"}
check(*d)'''


'''def check1(*a):
    d=1
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6)
check1(2,3,4,5,2.3,2.6)
check1(3,4,5,2,1.8,2.1,"python")'''


#**(kwargs)
#keyword variable length argument

'''def check2(**a):
    print(a)
    print(type(a))
check2()
details={"name":["suji","viji","suni","yashu"],
         "marks":[90,50,20,70],
         "status":["p","a","p","a"]}
check2(**details)'''


'''def check2(**a):
     print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(a,a[i])
    for i in a.items():
        print(i)
check2()
details={"name":["suji","viji","suni","yashu"],
         "marks":[90,50,20,70],
         "status":["p","a","p","a"]}
check2(**details)'''


'''def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i, j in b.items():
        print("key is",i)
        print("value are",j)

final()
data=(1,3,2,4,3.6,1.2)
#final(*data)
details={"year":[2024,2025,2026],
         "month":["june","july","aug"]}
#final(**details)
final(*data,**details)'''


#mini project
#railway ticket
'''while True:
    def railway():
        ticket= 1000
        option=int(input("select the option 1.Female 2.Male"))
        if option==1:
            age=int(input("enter the age:"))
            if age>=60:
                print(ticket-50/100*ticket)
            elif age<60:
                print((ticket-30/100*ticket))
        if option==2:
            age=int(input("enter the age:"))
            if age>=60:
                print(ticket-30/100*ticket)
            elif age<60:
                print(ticket)
    railway()'''




































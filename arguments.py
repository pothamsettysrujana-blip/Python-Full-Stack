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




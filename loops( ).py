#loops()
#for,while,range,break,continue,pass
#for loop()

'''a=[20,30,40,50]
for i in a:
    print(i)'''


'''a=[20,30,40,50]
for i in a:
    print(a)'''

'''a=[20,30,40,50]
for i in a:
    print(i,end=" ")'''

'''a=[20,30,40,50]
for i in a:
    print(i)
print(type(a))
print(type(i))'''


'''a=(2,3,4,5,6)
for i in a:
    print(i)
print(type(a))
print(type(i))'''


'''a={2,3,4,5,6}
for i in a:
    print(i)
print(type(a))
print(type(i))'''


'''a={"year":2026,"month":"july","date":9}
for i in a:
    print(i)
    print(type(a))
    print(type(i))
for i in a.keys():
    print(i)
for i in a.values():
    print(i)
    print(type(a))
    print(type(i))
for i in a.items():
    print(i)
    print(type(a))
    print(type(i))'''


'''a="codegnan"
for i in a:
    print(i)'''


'''b=[2.3,4.5,6.1]
for i in b:
    print(i)
    print(type(b))
    print(type(i))'''


'''b=["python","java","c","c++"]
for i in b:
    print(i)
    print(type(b))
    print(type(i))'''

'''b=[2+3j,4+5j]
for i in b:
    print(i)
    print(type(b))
    print(type(i))'''

'''b=[True,False]
for i in b:
    print(i)
    print(type(b))
    print(type(i))'''

#task
'''fruits=["apple","banana","mango"]

b=str(fruits)
print(b.upper())'''

'''for i in fruits:
    print(i.upper(),end=" ")'''

'''b=[]
for i in fruits:
    b.append(i.upper())
print(b)'''

#[1, 3, 5, 7, 9, 'code', 'c', 'o', 'd', 'e']
'''a=[1,3,5,7,9,"code"]
a.extend("code")
print(a)'''


#10-7-26

#while loop()
'''a=10
while a>1:
    print(a)'''

'''a=10
while a<1:
    print(a)'''

'''a=10
while a>1:
    print(a)
    a=a-1'''

'''a=20
while a>3:
    print(a)
    a=a-1'''

'''a=20
while a>3:
    a=a-1
    print(a)'''

'''a=20
while a>3:
    a=a-1
print(a)'''


'''a=40
while a>5:
    a=a-1
print(a)'''

'''a=30
while a>1:
    print(a)
    a+=1'''

'''a=10
while a>2:
    print(a)
    a-=1'''

'''a=30
while a>1:
    print(a)
    a-=1'''

'''a=1
while a<25:
    print(a)
    a+=1'''

#real time example
#bakery
'''while True:
    bakery = int(input("price:"))
    if bakery == 1200:
        print("redvelvet cake")
    elif bakery == 100:
        print("almond cake")
    elif bakery ==800:
      print("choclate cake")
    elif bakery == 600:
     print("butter scotch cake")
    else:
        print("cake is not available")'''

#voting
'''while True:
    a=int(input("age:"))
    if a>=18:
        print("eligible for vote")
    else:
        print("not eligible for vote")'''


#range()
#start-stop-step

'''for i in range(20):
    print(i)'''
        
'''for i in range(13,35):
    print(i)'''
   
'''for i in range(0,30,3):
    print(i,end=" ")'''

'''for i in range(5,50,5):
    print(i,end=" ")'''

'''for i in range(2,20,2):
    print(i,end=" ")'''

'''#grade code
while True:
    marks=int(input("enter the marks:"))
    if marks in range(91,101):
        print("Grade-A")
    elif marks in range (81,91):
        print("Grade-B")
    elif marks in range (71,81):
        print("Grade-c")
    elif marks in range (61,71):
        print("Grade-D")
    else:
        print("fail")'''



#break
'''a=10
while a>1:
    print(a)
    a=a-1'''

'''a=10
while a>1:
    print(a)
    a=a-1
    if a==6:
        break'''

'''a=10
while a>1:
    a=a-1
    if a==6:
        break
    print(a)'''

'''for i in range(20):
    if i==14:
        break
    print(i)'''

'''a="python"
if a=="h":
    break
print(a)'''#error

'''a="python"
for i in a:
    if i=="h":
        break
    print(i)'''

#continue
'''a=20
while a>5:
    print(a)
    a=a-1'''

'''a=20
while a>5:
    print(a)
    a=a-1
    if a==10:
        continue'''

'''a=20
while a>5:
    a=a-1
    if a==10:
        continue
    print(a)'''

'''for i in range(15):
    if i==7:
        continue
    print(i)'''

'''a="yasaswini"
for i in a:
    if i=="s":
        continue
    print(i)'''
#pass
#placeholder
'''a=30
while a>10:
    print(a)
    a=a-1
    if a==20:
        pass'''

'''for i in range(40):
    if i==10:
        pass
    print(i)'''















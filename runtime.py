#print(2+3)
'''a=5
b=3
print(a+b)'''


'''a=5
b=3
c=(a+b)
print(c)'''


#run_time input()
'''a=int(input("enter the a value:"))
b=int(input("enter the b value:"))
print(a+b)'''


'''a=float(input("enter the a value:"))
b=float(input("enter the b value:"))
print(a+b)'''


'''a=str(input("data 1:"))
b=str(input("data 2:"))
print(a+b)'''


'''a=input("data 1:")
b=input("data 2:")
print(a+b)'''


'''fname=input("data 1:")
lname=input("data 2:")
print((fname+" "+lname).title())'''


'''a=complex(input("data 1:"))
b=complex(input("data 2:"))
print(a+b)'''


'''a=bool(input("data 1:"))
b=bool(input("data 2:"))
print(a+b)'''


'''a=bool(input("data 1:"))
b=bool(input("data 2:"))
c=bool(input("data 3:"))
print(a+b+c)'''


'''a=int(input("a value"))
b=int(input("b value"))
option=int(input("choose the option 1.add 2.sub 3.mul"))
print(a+b)
print(a-b)
print(a*b)'''


'''a=int(input("a value"))
b=int(input("b value"))
option=int(input(choose the option
                 1.add
                 2.sub
                 3.mul))
print(a+b)
print(a-b)
print(a*b)'''


'''a=int(input("a value"))
b=int(input("b value"))
option=(input("choose the option add sub mul"))
print(a+b)
print(a-b)
print(a*b)'''


'''a=input()
print(a)'''


'''a=int(input())
b=int(input())
print(a+b)'''


#swppping of two variables

#integer()
'''a=10
b=20

temp=a
a=b
b=temp
print(a)
print(b)'''


'''a=10
b=20

a,b=b,a
print(a)
print(b)'''


'''a=10
b=20

a=a+b
b=a-b
a=a-b
print(a)
print(b)'''

'''a=10
b=20

a=a+b
b=a-b
a=a-b
print("after swapping a=%d,b=%d"%(a,b))'''

#string

'''a="srjana"
b="viji"
temp=a
a=b
b=temp
print(a)
print(b)'''


'''a="srjana"
b="viji"
a,b=b,a
print(a)
print(b)'''


'''a=input()
b=input()
a,b=b,a
print("after swapping a=%s,b=%s"%(a,b))'''


#float()

a=float(input())
b=float(input())

a=a+b
b=a-b
a=a-b
print("after swapping a=%.2f,b=%.2f"%(a,b))

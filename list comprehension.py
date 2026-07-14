#list comprehension
a=["codedgnan","python","course"]
#["CODEGNAN","PYTHON","COURSE"]
#print(a.upper())

'''b=str(a)
print(b.upper())'''

'''for i in a:
    print(i.upper(),end=",")'''

'''b=[]
for i in a:
    b.append(i.upper())
print(b)'''

#using list comprehension
#syntax
#a=[exprfor var in collection/range]
'''a=[i.upper() for i in a]
print(a)'''

'''a=["vij","hyd","vzg"]
#
a=[i.title() for i in a]
print(b)'''


'''b=[1,2,3,4,5,6,8,12,13]
b=[i**2 for i in b]
print(b)'''
'''b=[i*i for i in a]
b=[pow(i,2) for i in a]'''

#if usage in list comprehension
'''for i in range(0,16):
    print(i,end=" ")'''
    
'''a=[i for i in range(16)]
print(a)'''

'''a=[i for i in range(16) if i%2==0]
print(a)'''

'''a=[i for i in range(16) if i%2!=0]
print(a)'''

'''a=[i**2 for i in range(21) if i%2==0]
print(a)'''
    
'''a=["appple","banana","grapes","mango","kiwi","dragon","berry"]
b=[i for i in a if "a" in i]
print(b)

a=["appple","banana","grapes","mango","kiwi","dragon","berry"]
b=[i for i in a if "a" not in i]
print(b)'''

#no elif usage in list comprehension

#if-else usage

'''a=[i**2 if i%2==0 else i*5 for i in range(31)]
print(a)'''

a=[1,2,3,4,5]
b=[5,4,3,2,1]
#6,6,6,6,6
c=[a[i]+b[i] for i in range(len(a))]
print(c)

c=[a[i]+b[i] for i in range(5)]
print(c)

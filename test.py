#print("hello world")
"""
this is first code in python
"""
#print(12)
x=12
y=23.5
x='shamma'

#print(z)
print(y)

"""type casting"""
x=str(3)
y=int(23.5)
z=float(25)
#print(x)
#print(y)
#print(z)


"""get type of variable"""
x=5
y='shamma'
print(type(x))
print(type(y))

#output <class 'int'>

#case sensitive cases
a=4
A="tuktuk"

print(a)
print(A)

#multiple values
x,y,z="lamisa",1018,"shamma"
print(x)
print(y)
print(z)


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


print("output is "+x+" fruit")
print(x+y)



def myfunc():
   global b
   b="quaiyum"


myfunc()
print(b)

z=1j
print(type(z))

x = 3+5j
y = 35656222554887711
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

import random
print(random.randrange(1,10))

a="""helloasjfkjhsdjfkdfdsfdjfndj,
  sfsdfdsfsdfds,
  "dsfsdfsdfdsfdsf."""

print(a)

a = "Hello, World!"
print(a[6])

for x in "banana":
    print(x)
print(len(a))

print("World" in a)

if "Hello" in a:
 print("Yes")


b = "Hello, World!"
print(b[-5:-2])

a = "Hello, World!"
print(a.upper())
print(a.lower())
print(a.replace("H" , "o"))
print(a.split(","))


age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


a=12
sd=34
t="this is my {} and that is yours {}."
print(t.format(a,sd))


txt = "banana"

x = txt.center(30)

print(x)


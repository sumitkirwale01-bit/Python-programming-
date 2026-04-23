#list
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(a)
print(type(a))

abc=[10,20,30,40,50,60,70,80,90,100]
print(abc)

#Concatination
d=a+abc
print(d)

print(len(d))

#append Operation
d.append(200)
print(d)

#remove Operation
d.remove(200)
print(d)

#Slicing Operation
print(d[6:])
print(d[-20:-1])

#Sort Operation
d.sort()
print(d)

#Reverse Operation
d.reverse()
print(d)
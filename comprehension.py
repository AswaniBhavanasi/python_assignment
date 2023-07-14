#list compreshion
print([i for i in range(1,10)])
# dict compreshion
keys=['a','b','c','d']
values=[1,2,3,4]
mydict={k:v for (k,v) in zip(keys,values)}
print(mydict)
# tuple compreshion
t=tuple([i for i in range(1,10)])
print(t)

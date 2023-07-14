#__init__
'''
class bookname:
    def __init__(self,title):
        self.title=title
    def book(self):
        print('the title of the book is',self.title)

b=bookname('Ramayanam')
b.book()
'''
# with
'''
with open('myfile.txt','w') as file:
    file.write('this is monday')'''
# list compreshion
'''print([i for i in range(1,10)])'''
# dict compreshion
'''keys=['a','b','c','d']
values=[1,2,3,4]
mydict={k:v for (k,v) in zip(keys,values)}
print(mydict)'''
# tuple compreshion
'''t=tuple([i for i in range(1,10)])
print(t)'''

#string slicing
'''st='bindu'
print(st[1::3])'''

#to print 1 to 100 prime numbers
'''n1=int(input('enter a first number:'))
n2=int(input('enter a second number:'))
for i in range(n1,n2+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)'''
#exception handling
'''try:
    n1=int(input('enter a number:'))
    n2=int(input('enter a another number:'))
    n=n1/n2
except ValueError:
    print('invalid number')
except ZeroDivisionError:
    print('zerror occured')
finally:
    print('the result is come:')
'''
# list is mutable
'''lst=[1,2,3,5]
lst.append('ashu')
print(lst)

lst.remove(3)
print(lst)
'''
#tuple is immutable
'''t=(1,2,4)
t.append(3)
print(t)'''

#.What is the difference between merge, join and concatenate?
import pandas as pd
'''d1=pd.DataFrame({'id':[1,2,3,4],'name':['ashu','mani','sam','nani'],'sal':[1000,2000,3000,4000]})
d2=pd.DataFrame({'id':[1,2,5,6],'name':['advik','raja','lahari','sandy'],'marks':[20,30,40,50]})
mergeset=pd.merge(d1,d2,on='id')
print(mergeset)'''
'''
d1=pd.DataFrame({'id':[1,2,3,4],'name':['sai','ravi','lucky','bharat']})
d2=pd.DataFrame({'id':[1,2,4,5],'name':['aswani','keerthi','sandya','sree']})
con=pd.concat([d1,d2])
print(con)
'''
'''
d1=pd.DataFrame({'id':[1,2,3,4],'name':['sai','nani','mani','ravi']})
d2=pd.DataFrame({'id':[2,3,5,6],'age':[22,30,50,66]})
a=d1.join(d2.set_index('id'),on='id',how='inner')
print(a)

'''
# why use else in try/except construct in python
'''try:
    n1=int(input('enter a number:'))
    n2=int(input('enter a another number:'))
    result=n1/n2
except ValueError:
    print('invalid number')
except ZeroDivisionError:
    print('zero occurred')
else:
    print('the division was successful')
    print('result',result)'''
    














                







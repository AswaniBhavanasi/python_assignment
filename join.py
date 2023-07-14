#join
import pandas as pd

d1=pd.DataFrame({'id':[1,2,3,4],'name':['sai','nani','mani','ravi']})
d2=pd.DataFrame({'id':[2,3,5,6],'age':[22,30,50,66]})
a=d1.join(d2.set_index('id'),on='id',how='inner')
print(a)

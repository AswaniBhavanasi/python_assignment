#merge
import pandas as pd
d1=pd.DataFrame({'id':[1,2,3,4],'name':['ashu','mani','sam','nani'],'sal':[1000,2000,3000,4000]})
d2=pd.DataFrame({'id':[1,2,5,6],'name':['advik','raja','lahari','sandy'],'marks':[20,30,40,50]})
mergeset=pd.merge(d1,d2,on='id')
print(mergeset)

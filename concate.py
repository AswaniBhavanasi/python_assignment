#concate
import pandas as pd
d1=pd.DataFrame({'id':[1,2,3,4],'name':['sai','ravi','lucky','bharat']})
d2=pd.DataFrame({'id':[1,2,4,5],'name':['aswani','keerthi','sandya','sree']})
con=pd.concat([d1,d2])
print(con)

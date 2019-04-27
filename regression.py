import pandas as p
import numpy as n
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plot



data=p.read_csv('datasheet.csv',header=0)
data=data.dropna()
print(list(data.columns))

data['education']=n.where(data['education']=='Bachelors','BA',data['education'])

# print(data)

smth=data.groupby('applied').mean()
# print(smth)


p.crosstab(data.job,data.applied).plot(kind='line')
plot.title('Apply for loan by job title')
plot.xlabel('Job')
plot.ylabel('Total Applied for Loan')
plot.savefig('purchaseplot')

df=p.DataFrame({'col1':[5,2,3,4],
                'col2':['a','b','v','sf'],
                'col3':['p2',4,'fgs',3]})

df.sort_values(by=['col1'])
# print(df)

mylist=[2,3,5,8,3,1,9,55,3,2,455,7677]
mysecondlist=[3,5,6,2,1,5,3,455,7677]

newlist=set(mylist)
newlist2=set(mysecondlist)

difference=newlist ^ newlist2 # symmetric difference, what is unique to each set
difference2=newlist.difference(newlist2) #difference, what is in the first, but not in second

union_my=newlist.union(newlist2)
union_list=list(union_my)
print(union_list)

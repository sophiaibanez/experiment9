import pandas as pd

a = {'Student':['Ice Bear','Panda','Grizzly'], 'Math':[80,95,79]}
b = {'Student':['Ice Bear','Panda','Grizzly'], 'Electronics':[85,81,83]}
c = {'Student':['Ice Bear','Panda','Grizzly'], 'GEAS':[90,79,93]}
d = {'Student':['Ice Bear','Panda','Grizzly'], 'ESAT':[93,89,88]}
A = pd.DataFrame(a, columns=['Student','Math'])
B = pd.DataFrame(b, columns=['Student','Electronics'])
C = pd.DataFrame(c, columns=['Student','GEAS'])
D = pd.DataFrame(d, columns=['Student','ESAT'])

x = pd.merge(A,B,how='right',on='Student')
y = pd.merge(x,C,how='right',on='Student')
z = pd.merge(y,D,how='right',on='Student')

melted = pd.melt(z, id_vars = 'Student', value_vars = ['Math','Electronics','GEAS','ESAT'])
finalMelt = melted.rename(columns = {'variable':'Subject','value':'Grades'})

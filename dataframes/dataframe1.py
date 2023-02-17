import pandas as pd 

d = {'name': ['Braund', 'Cummings', 'Heikkinen', 'Allen'],
     'age': [22,38,26,35],
     'fare': [7.25, 71.83, 0 , 8.05], 
     'survived?': [False, True, True, False]}

df = pd.DataFrame(d)

print(df)
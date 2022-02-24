#%%
import numpy as np
import pandas as pd

#%%
zoo = pd.DataFrame({ 'city':["Tokyo","Tokyo","Tokyo","Fukuoka","Fukuoka"],
                    'since':[1950, 2001, 1977, 1988, 1992],
                    'lion':[5,2,3,0,1],
                    'kapybara':[6,9,12,4,2]
})
zoo

#%% [markdown]
# Want to operate some like SQL window function at pandas..
# ```
# select *, row_number() over(partition by city order by since)
# from zoo 
# ```

#%%
df = zoo.copy()
df = df.sort_values('since') 
df['row_number'] = np.arange(len(df.index))
df['order'] = df.groupby(by=['city'])['row_number'].transform(lambda x: x.rank())
df

#%%
df = zoo.copy()
df = df.sort_values('since') 
df['order'] = df.groupby(by=['city']).cumcount()
df

#%% [markdown]
# ```
# select * from(
#     select *, row_number() over(partition by city order by since) as row_number
#     from zoo 
# )
# where row_number = 1
# ```
# or as bigquery,
# ```
# select *, row_number() over(partition by city order by since) as row_number
# from zoo 
# qualify row_number = 1
# ```

#%%
df = zoo.copy()
df = df.sort_values('since') 
df = df.groupby(by=['city']).head(1)
df

#%%
df = zoo.copy()
df = df.sort_values('since') 
df = df.groupby(by=['city']).nth(0)
df

#%%
df = zoo.copy()
df = df.sort_values('since') 
df = df.groupby(by=['city']).first()
df

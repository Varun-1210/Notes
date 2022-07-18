# Python
# Indexing, Selection, and Filtering

# Series indexing (obj[...]) works analogously to NumPy array indexing, except you can use the Series’s index values instead of only integers.

from operator import index
import pandas as pd
import numpy as np

data = pd.Series(np.arange(4,dtype=int),index=list('abcd'))
print(data)

data[1] # indexing using integer
data['c'] # indexing using index label
data[1:3] # slicing 
data['a':'c'] # Slicing with labels behaves differently than normal Python slicing in that the endpoint is inclusive

data[['a','c','b','d']] # changing the order
data[[2,1,0,3]] # changing the order
data[data <= 2] # Boolean indexing

# Setting using these methods modifies the corresponding section of the Series
data['a':'c'] = 12
print(data)

# Indexing into a DataFrame is for retrieving one or more columns either with a single value or sequence:

data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 'Colorado', 'Utah', 'New York'],columns=['one', 'two', 'three', 'four'])

print(data)
data['two']
data[['four','two']]
data[0:3] # Single indexing wont working 
data[data.three > 5] # boolean indexing

data[data < 5] = 'Hola' # True values will be replaced 

####################################################################################################

# Selection with loc and iloc

# For DataFrame label-indexing on the rows, I introduce the special indexing operators loc and iloc. They enable you to select a subset of the rows and columns from a DataFrame with NumPy-like notation using either axis labels (loc) or integers (iloc).

data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 'Colorado', 'Utah', 'New York'],columns=['one', 'two', 'three', 'four'])

data.loc['Colorado',['three','one']] # Using index labels
data.iloc[1,[2,0]] # same as above but using index

data.iloc[0] # always [row,column] --> here first row

# list(enumerate(data.index))
# list(enumerate(data.columns))

data.iloc[[2,1],[3,1,2]] # multiple columns and rows 

data.loc['Ohio':'Utah','two':] # slicing will work for both index and labels also

data.iloc[:,:3][data.three > 5] # condition along with filter

data.at['Colorado','three'] # returns value connecting Colorado and three
data.iat[1,1]  # returns value connecting 1st row and 1st column
data.reindex(['one', 'two', 'three', 'four','five'],axis=1)
# data.reindex(data.columns.append(pd.Index(['five'])),axis=1)

data.reindex(data.columns.to_list()+['five'],axis=1)
data.reindex(index = data.index.to_list()+['India'],columns=data.columns.to_list()+['five'])


# data[val] --> selecting single column
# data.loc[val] --> selecting single row
# data.loc[:,val] --> selecting single column
# data.loc[val_1,val_2] --> selecting both row and column
# data.iloc[where] --> selecting row by position
# data.iloc[:, where] --> selecting column by position
# data.iloc[where_i, where_j] --> selecting row and column by position
# data.at[label_i, label_j] --> Select a single scalar value by row and column label 
# data.iat[i, j] --> Select a single scalar value by row and column position (integers)

####################################################################################################

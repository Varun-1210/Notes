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
data['a':'c'] # slicing
data[['a','c','b','d']] # changing the order
data[[2,1,0,3]] # changing the order


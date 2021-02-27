from pandas import Series, DataFrame 
import pandas as pd 
import numpy as np 


# Example from - https://chrisalbon.com/python/pandas_map_values_to_values.html

# can be put in dict form, but it is not used well.
raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
        'age': [42, 52, 36, 24, 73],
        'city': ['San Francisco', 'Baltimore', 'Miami', 'Douglas', 'Boston']}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'city'])
df

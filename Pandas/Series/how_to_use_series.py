from pandas import Series
import pandas as pd 
import numpy as np


list_data = [5, 6, 7, 8, 9] 
ex_obj = Series(data = list_data)  # Index name can also be specified
ex_obj


# access to data index
ex_obj["a"]


# Assign a value to the data index
ex_obj["a"] = 3.2
ex_obj

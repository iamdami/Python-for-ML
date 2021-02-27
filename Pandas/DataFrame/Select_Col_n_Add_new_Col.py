from pandas import Series, DataFrame 
import pandas as pd 
import numpy as np


# Select Column
DataFrame(raw_data, columns = ["age", "city"])


# Add a new Column
DataFrame(raw_data, columns = ["first_name","last_name","age", "city", "debt"] 
         )

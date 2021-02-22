import numpy as np 

# load txt 
txt = np.loadtxt(".txt")
txt[:10]

# Convert the imported txt to int type and load up to the 3rd index
txt_int = txt.astype(int) 
txt_int[:3]

# save txt
np.savetxt('int_data.csv', txt_int, delimiter=",")

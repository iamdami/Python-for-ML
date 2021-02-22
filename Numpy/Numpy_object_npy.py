import numpy as np

np.save("npy_test", arr=txt_int)

# Load up to the 3rd index of the file 
npy_array = np.load(file="npy_test.npy") 
npy_array[:3]

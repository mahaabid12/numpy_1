import numpy as np 

a=np.arange(10,34,1).reshape(8,3)

print(np.array_split(a,4))
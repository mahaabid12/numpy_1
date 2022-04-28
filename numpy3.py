import numpy as np
arrayOne= np.array([[5,6,9],[21,18,27]])
arrayTwo= np.array([[15,33,24],[4,7,1]])


numpy=np.concatenate((arrayOne,arrayTwo), axis=1)

squrenp=np.square(numpy)
print(squrenp)
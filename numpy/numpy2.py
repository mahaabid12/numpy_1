import numpy as np
tab= np.arange(start=0, stop=9).reshape(3,3)
tab2=[]

#extacting elements in tab2 and then extracting 
# the element in the third column 

for e in tab : 
    tab2.append(e[2])

    
print (tab2)
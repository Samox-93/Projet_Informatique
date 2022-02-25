import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img





data = np.load('/Users/samiamrouni/Downloads/newdosi_1_200403290A_19870601_ground_truth.npy')
print(data)

data1=data[:,:,100]

#for i in range(128):
    #for j in range(32):
        #if data1[j,i] > 0:
            #data1[j,i]=1
        

plt.imshow(data1,cmap="gray")
plt.show()








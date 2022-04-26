import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
import open3d as o3d

path = '/Users/samiamrouni/Downloads/newdosi_1_200403290A_19870601_ground_truth.npy'
path1= '/Users/samiamrouni/Downloads/newdosi_1_200403290A_19870601_output_NN.npy'
    

#test


somme = 0
somme_quadratique = 0   
ground = np.load(path)
output = np.load(path1)
m = ground.shape[0]*ground.shape[1]*ground.shape[2]
cpt = 0

for i in range(ground.shape[0]):
    for j in range(ground.shape[1]):
        for k in range(ground.shape[2]):
        
                somme += np.abs(ground[i,j,k]-output[i,j,k])
                somme_quadratique += np.abs((ground[i,j,k]-output[i,j,k])**2)
                cpt += 1

MAE = somme/cpt
MSE = somme_quadratique/cpt                
                             
print("MAE =", MAE)
print("MSE =", MSE)                

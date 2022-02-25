import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
import open3d as o3d
import os.path

data = "/Users/samiamrouni/Dataset_projet_info/"

path = '/Users/samiamrouni/Downloads/newdosi_1_200403290A_19870601_ground_truth.npy'
path1 = '/Users/samiamrouni/Downloads/newdosi_1_200403290A_19870601_output_NN.npy'


def MAE_MSE(path,path1):

    ground = np.load(path)
    output = np.load(path1)
    val_max = 0
    for i in range(ground.shape[0]):
        for j in range(ground.shape[1]):
            for k in range(ground.shape[2]):
                if ground[i,j,k] > val_max:
                    val_max = ground[i,j,k]

    somme = 0
    somme_quadratique = 0   
    m = ground.shape[0]*ground.shape[1]*ground.shape[2]
    cpt = 0

    local_max = 0.05*val_max


    for i in range(ground.shape[0]):
        for j in range(ground.shape[1]):
            for k in range(ground.shape[2]):
                if ground[i,j,k] < local_max:
                    somme += np.abs(ground[i,j,k]-output[i,j,k])
                    somme_quadratique += np.abs((ground[i,j,k]-output[i,j,k])**2)
                    cpt += 1

    MAE = somme/cpt
    MSE = somme_quadratique/cpt
    
    return(MAE,MSE)



    #print("MAE =", MAE)
    #print("MSE =", MSE)


ground = []
output = []

Diff_shape_ground = []
Diff_shape_output = []

alone_GD = []
alone_output = []

autre = []

for root, dirs, files in os.walk(data, topdown=False):
   for name in files:
       ID = name[:30]
       if 'ground_truth.npy' in name:
           # print(os.path.join(root, name))
           # print(os.path.join(root, name[:30] + 'output_NN.npy'))
           if os.path.isfile(os.path.join(root, name.split('ground_truth')[0] + 'output_NN.npy')):
               if (np.load(os.path.join(root, name.split('ground_truth')[0] + 'output_NN.npy')).shape) == (np.load(os.path.join(root, name)).shape):
                       output.append(os.path.join (root, name.split('ground_truth')[0] + 'output_NN.npy'))
                       ground.append(os.path.join(root, name))
               else : 
                   Diff_shape_output.append(os.path.join(root, name.split('ground_truth')[0] + 'output_NN.npy'))
                   Diff_shape_ground.append(os.path.join(root, name))
               # sys.exit()
           else: 
               alone_GD.append(os.path.join(root, name))
              
       elif 'output_NN.npy' in name:
           if not os.path.isfile(os.path.join(root, name.split('output_NN')[0] + 'ground_truth.npy')):
               alone_output.append(os.path.join(root, name))
               
#Classer les MAE et les MSE dans des listes, calculer la moyenne et l'ecart-type

#print(ground)
#print(output)

Mae = []
Mse = []

for loop in range(len(ground)):
    (x,y) = MAE_MSE(ground[loop],output[loop])
    Mae.append(x)
    Mse.append(y)
Mae_moyenne = np.mean(Mae)   
Mse_moyenne = np.mean(Mse)
Mae_et = np.std(Mae)
Mse_et = np.std(Mse)

print("Moyenne MAE =",Mae_moyenne)
print("Moyenne Mse =",Mse_moyenne)

print("Ecart-Type de Mae =",Mae_et)
print("Ecart-Type de Mse =",Mse_et)


print("Moyenne MAE =",Mae_moyenne,"±",Mae_et)
print("Moyenne MSE =",Mse_moyenne,"±",Mse_et)


        
    
    
    
    
               

       
    
   

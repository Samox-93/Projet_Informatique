import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
import open3d as o3d

data= np.load('/Users/samiamrouni/Downloads/newdosi_1_200403290A_19870601_ground_truth.npy')
posi = np.empty(3)
inte = np.empty(1)
for i in range(128):
    for j in range(32):
        for k in range(32):
            if data[k,j,i] > 0:
                row = np.array([k,j,i])
                posi = np.vstack([posi,row])
                row2 = data[k,j,i]
                inte = np.vstack([inte,row2])
                
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(posi)
o3d.visualization.draw_geometries([pcd])
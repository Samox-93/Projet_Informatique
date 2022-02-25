import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
import open3d as o3d

def corps(path,defletion):
    data= np.load(path)

    posi = []
    inte = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            for k in range(data.shape[2]):
                if data[i,j,k] > 0:
                    posi.append([i,j,k])
                    inte.append(data[i,j,k])


    inte2 = []
    for i in range(len(inte)):
        inte2.append(inte[i]+0.5)
        colors = plt.get_cmap("Greys")(inte2)

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(posi)
    pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])
    #o3d.visualization.draw_geometries([pcd])
    downpcd = pcd.voxel_down_sample(voxel_size=defletion)
    o3d.visualization.draw_geometries([downpcd])
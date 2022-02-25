import pymedphys
import numpy as np
from pymedphys import gamma



path = "/Users/samiamrouni/Downloads/newdosi_1_200403290A_19870601_ground_truth.npy"
path2 = "/Users/samiamrouni/Downloads/newdosi_1_200403290A_19870601_output_NN.npy"

ground = np.load(path)
output = np.load(path2)

x = (np.linspace(0,32,32))
y = (np.linspace(0,32,32))
z = (np.linspace(0,128,128))
coords = (x,y,z)


axe_ref = axe_eva = coords

gam = pymedphys.gamma.gamma_shell(axe_ref, ground, axe_eva, output, 1,1)


gam2 = pymedphys.gamma.calculate_pass_rate(gam)
print(gam2)


import pydicom as py
import numpy as np
import matplotlib.pyplot as plt

path = "/Users/samiamrouni/Downloads/CT1520696-TDM_RT_CRANE-TETE__3_0__H20s-20100415/5_TETE__3_0__H20s-40.dcm"

ds = py.read_file(path)

plt.imshow(ds.pixel_array, cmap=plt.cm.bone)

print(ds[0x00100010])
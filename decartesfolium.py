import numpy as np 
import matplotlib.pyplot as plt 

fi = np.arange(0, np.pi * 2, 0.001)

p = 3*np.cos(fi)*np.sin(fi)/(np.cos(fi) ** 3 + np.sin(fi) ** 3)

x = p * np.cos(fi)
y = p * np.sin(fi)

plt.plot(x, y)
plt.axis([-2, 2, -2, 2])
plt.savefig("decartesfolium.png") 
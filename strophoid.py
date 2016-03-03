import numpy as np 
import matplotlib.pyplot as plt 

fi = np.arange(0, np.pi * 2, 0.001)

p = -1*np.cos(2*fi)/np.cos(fi)

x = p * np.cos(fi)
y = p * np.sin(fi)

plt.plot(x, y)
plt.axis([-1, 1.5, -1, 1])
plt.savefig("strophid.png") 
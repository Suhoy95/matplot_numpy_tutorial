import numpy as np 
import matplotlib.pyplot as plt 

fi = np.arange(0, np.pi * 2, 0.001)

p = -(np.cos(2*fi) - 1)/np.cos(fi)

x = p * np.cos(fi)
y = p * np.sin(fi)

plt.plot(x, y)
plt.axis([0, 1.99, -2, 2])
plt.savefig("cissoid.png") 
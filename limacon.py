import numpy as np 
import matplotlib.pyplot as plt 

fi = np.arange(0, np.pi * 2, 0.001)


for r in np.arange(0.5, 4, 0.5):
    p = r*np.cos(fi) + 1

    x = p * np.cos(fi)
    y = p * np.sin(fi)
    plt.plot(x, y)

plt.axis([-1, 5, -3, 3])
plt.savefig("limacon.png") 
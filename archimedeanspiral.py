import numpy as np 
import matplotlib.pyplot as plt 

fi = np.arange(0, 2*np.pi * 2, 0.001)


p = 1*fi

x = p * np.cos(fi)
y = p * np.sin(fi)
plt.plot(x, y)

plt.savefig("archimedeanspiral.png")

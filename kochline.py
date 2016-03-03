import numpy as np 
import matplotlib.pyplot as plt 
import sys

def snowflake(points = np.array([ [0, 0],
                             [0, 1]], 
                             dtype=np.float64),
              generation = 6):

    if generation == 0:
        return points;

    newPoint = np.array([points[0]]) 

    for i in xrange(1, points.shape[0]):
        a = points[i - 1]
        b = points[i]
        
        v = b - a
        ort = np.array([v[1], -v[0]])
        
        c = a + v / 3 
        d = a + 2 * v / 3
        e = a + v/2 + 0.866/3*ort
        newPoint  = np.vstack( (newPoint,  
                                np.array([c, e, d, b]))
                             )

    return snowflake(newPoint, generation - 1)
gen = 5
if len(sys.argv) > 1:
    gen = int.parse(sys.argv[1])

points = snowflake(generation = gen )


plt.plot(points[:, 1], points[:, 0])
plt.axis([0,1 ,0, 0.5])
plt.savefig("kochline.png") 
import numpy as np
import matplotlib.pyplot as plt 

print("Welocme to OHM'S GRAPHER !")
x = np.linspace(-2,2,1000000)
y = 2*x**2+10
plt.plot(x,y, ':k')
plt.title('Graph of your equation')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
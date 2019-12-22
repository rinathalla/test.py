import pandas as pd
from matplotlib import pyplot as plt
x= [1,2,3]
y= [3,7,9]
z=[6,3,1]
plt.plot(x,y)
plt.plot(x,z)
plt.title('Test Plot')
plt.xlabel("Y and Z")
plt.ylabel("X")
plt.legend(["X","Y"])
plt.show()
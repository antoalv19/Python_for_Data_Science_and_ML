import numpy as np
import matplotlib.pyplot as plt

# Data to be used for the exercise
x = np.arange(0, 100)
y = x * 2
z = x ** 2

# Exercise 1
# ** Follow along with these steps: **
# ** Create a figure object called fig using plt.figure() **
fig = plt.figure()

# ** Use add_axes to add an axis to the figure canvas at [0,0,1,1]. Call this new axis ax. **
ax = fig.add_axes([0, 0, 1, 1])
# ** Plot (x,y) on that axes and set the labels and titles to match the plot below:**
ax.plot(x, y)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("title")
plt.show(ax)

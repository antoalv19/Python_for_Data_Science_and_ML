import matplotlib.pyplot as plt
import numpy as np

# use: plt.show() at the end of all your plotting commands to have the figure pop up in another window.
# Let's walk through a very simple example using two numpy arrays.
# You can also use lists, but most likely you'll be passing numpy arrays or pandas columns.
x = np.linspace(0, 5, 11)
y = x ** 2
######################################## FUNCTIONAL PROGRAMMING ########################################################
# Basic Matplotlib Commands We can create a very simple line plot using the following:
plt.plot(x, y)
plt.xlabel("Asse X")
plt.ylabel("Asse Y")
plt.title("Titolo")

# Creating multi plots on a canvas - plt.subplot(nrows, ncols, plot_number)
# plot numero 1
plt.subplot(1, 2, 1)
plt.plot(x, y, "r--")
# plot numero 2
plt.subplot(1, 2, 2)
plt.plot(x, y, "g*-")

"""Matplotlib Object Oriented Method
The main idea in using the more formal Object Oriented method is to create figure objects and then just call methods
 or attributes off of that object. This approach is nicer when dealing with a canvas that has multiple plots on it. 
To begin we create a figure instance. Then we can add axes to that figure.
"""
# Create empty canvas
fig = plt.figure()

# add set of axes to the figure
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # left, bottom, width, height (range 0 to 1)

# Plot on that set of axes
axes1.plot(x, y, "b")

# Insert axes title and graph title
axes1.set_xlabel("Asse X Grande")
axes1.set_ylabel("Asse Y Grande")
axes1.set_title("Titolo del Grafico Grande")

# Code is a little more complicated, but the advantage is that we now have full control
# of where the plot axes are placed, and we can easily add more than one axis to the figure:
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])  # left, bottom, width, height (range 0 to 1)

# plot the second graph
axes2.plot(x, y, "r--")

# Insert axes title and graph title
axes2.set_xlabel("Asse X Piccolo")
axes2.set_ylabel("Asse Y Piccolo")
axes2.set_title("Titolo Grafico Piccolo")

#################################################### START OF SUBPLOTS #################################################

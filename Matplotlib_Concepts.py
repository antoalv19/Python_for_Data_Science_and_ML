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
# The plt.subplots() object will act as a more automatic axis manager.
# Use similar to plt.figure() except use tuple unpacking to grab fig and axes
fig, axes = plt.subplots()

# Now use the axes object to add stuff to plot
axes.plot(x, y, 'r')
axes.set_xlabel('Asse X')
axes.set_ylabel('Asse Y')
axes.set_title('Subplots')

# Then you can specify the number of rows and columns when creating the subplots() object:
fig, axes = plt.subplots(nrows=1, ncols=2)

# AXES is an iterable array of axes to plot on
for ax in axes:
    ax.plot(x, y, "b")
    ax.set_xlabel("Asse X")
    ax.set_ylabel("Asse Y")
    ax.set_title("Titolo due")

# We can use fig.tight_layout() or plt.tight_layout() method,
# which automatically adjusts the positions of the axes on the figure canvas so that there is no overlapping content:

plt.tight_layout()

"""Figure size, aspect ratio and DPI
Matplotlib allows the aspect ratio, DPI and figure size to be specified when the Figure object is created.
You can use the figsize and dpi keyword arguments.

figsize is a tuple of the width and height of the figure in inches
dpi is the dots-per-inch (pixel per inch)."""
fig = plt.figure(figsize=(8, 4), dpi=100)

# The same arguments can also be passed to layout managers, such as the subplots function:
fig, axes = plt.subplots(figsize=(12, 3))
axes.plot(x, y, 'r')
axes.set_xlabel('Asse X')
axes.set_ylabel('Asse Y')
axes.set_title('Subplots')


# Saving figures
# Matplotlib can generate high-quality output in a number formats, including PNG, JPG, EPS, SVG, PGF and PDF.
# To save a figure to a file we can use the savefig method in the Figure class:
# fig.savefig("test_filesave_02122019.png", dpi=200)

# Legends
# You can use the label="label text" keyword argument when plots or other objects are added to the figure,
# and then using the legend method without arguments to add the legend to the figure:
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, x**2, label="x**2")
ax.plot(x, x**3, label="x**3")
ax.legend(loc=0)

# The legend function takes an optional keyword argument loc that can be used
# to specify where in the figure the legend is to be drawn.

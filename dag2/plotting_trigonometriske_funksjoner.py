"""

Eksempel med trigonometriske funksjoner
Demonstrerer også både linspace og arange

"""

from pylab import linspace, arange, sin, plot, show

#xverdier = linspace(-6, 6, 1000)
xverdier = arange(-6, 6, 0.01)

yverdier = sin(xverdier)

plot(xverdier, yverdier, "*-")
show()


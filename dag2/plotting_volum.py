"""

Eksempel på plotting.

"""

from pylab import linspace, plot, show, pi, xlabel, ylabel

def volum(radius):
    return 4/3*pi*radius**3

xverdier = linspace(0, 100, 30)
yverdier = volum(xverdier)

plot(xverdier, yverdier, "*-")

xlabel("Radius")
ylabel("Volum")

show()
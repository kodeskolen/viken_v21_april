"""

Eksempel som demonstrerer hvordan importere
Regner ut areal og omkrets av en sirkel

"""

from math import pi

radius = float(input("Hva er radiusen til sirkelen? "))

print(radius, type(radius))

areal = pi*radius**2
omkrets = 2*pi*radius

print(f"Omkretsen og arealet av en sirkel med radius {radius} " + \
      f"er {omkrets:.2f} cm, {areal:.2f} cm^2.")




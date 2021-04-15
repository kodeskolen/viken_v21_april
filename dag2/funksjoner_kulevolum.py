"""

Introduksjon til funksjoner: Kulevolum

"""

from math import pi

def volum(radius):
    return 4/3*pi*radius**3

radius_fotball = 24       # cm
volum_fotball = volum(radius_fotball)

print(f"Volum: {volum_fotball:.2f} cm^3.")

radius_golfball = 21    # mm
volum_golfball = volum(radius_golfball)

print(f"Volum: {volum_golfball:.2f} mm^3.")





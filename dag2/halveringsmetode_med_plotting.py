"""

Implementasjon av halveringsmetoden med plotting

"""

from pylab import sign, cos, linspace, plot, show, grid, xlim, ylim, axvline
from time import sleep

def f(x):
    return x**2 - 4

def midtpunkt(a, b):
    return (a + b)/2

min_verdi = -6
maks_verdi = 6
eps = 0.01
antall_gjett = 100

xverdier = linspace(-6, 6, 100)
yverdier = f(xverdier)

for gjett_nr in range(1, antall_gjett + 1):
    
    gjett = midtpunkt(min_verdi, maks_verdi) 
    
    funksjonsverdi = f(gjett)
    
    print(f"Jeg gjetter på {gjett}!")
    print(f"f({gjett}) = {funksjonsverdi}")
    
    if abs(funksjonsverdi) < eps:
        print("Jeg fant et nullpunkt!")
        print(f"f({gjett}) = {funksjonsverdi}")
        break
    elif sign(funksjonsverdi) == sign(f(min_verdi)):
        min_verdi = gjett
    else:      # elif sign(funksjonsverdi) == sign(f(maks_verdi))
        maks_verdi = gjett

    plot(xverdier, yverdier)
    xlim(-6, 6)
    ylim(-6, 6)
    
    axvline(min_verdi, color="orange")
    axvline(maks_verdi, color="orange")
    
    grid()
    plot([gjett], [funksjonsverdi], "o", color="red")
    show()
    
    sleep(1)
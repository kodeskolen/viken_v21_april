"""

Implementasjon av halveringsmetoden

"""

from pylab import sign, cos

def f(x):
    return cos(x) - x

def midtpunkt(a, b):
    return (a + b)/2

min_verdi = -6
maks_verdi = 6
eps = 0.01
antall_gjett = 100

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

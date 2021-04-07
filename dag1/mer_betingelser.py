"""

Program som demonstrerer litt mer om betingelser.

"""


tall = 9
faktor1 = 3
faktor2 = 5


if (tall % faktor1) == 0 and (tall % faktor2) == 0:
    print(f"Tallet {tall} er delelig på {faktor1} og {faktor2}.")
elif (tall % faktor1) == 0:
    print(f"Tallet {tall} er delelig på {faktor1}.")
elif (tall % faktor2) == 0:
    print(f"Tallet {tall} er delelig på {faktor2}.")
else:
    print(f"Tallet {tall} er hverken delelig på {faktor1} eller {faktor2}.")



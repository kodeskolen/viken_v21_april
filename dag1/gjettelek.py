"""

Gjettelek: Vi tenker på et tall, brukeren skal gjette hvilket det er.
Etter hvert forsøk sier vi om det er riktig, for høyt eller for lavt.

"""

from random import randint


fasit = randint(1, 1000)

antall_forsøk = 10

for gjett_nr in range(1, antall_forsøk + 1):
    
    gjett = int(input("Hvilket tall tror du jeg tenker på? "))
    
    if gjett == fasit:
        print(f"Det var riktig! Jeg tenkte på {fasit}.")
        break
    elif gjett < fasit:
        print("Det var dessverre feil. Du gjettet for lavt.")
    elif gjett > fasit:
        print("Det var dessverre feil. Du gjettet for høyt.")



    
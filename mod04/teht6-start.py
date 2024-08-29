# π ≈ 4n/N, jossa N on kaikkien pisteiden lukumäärä ja
# n yksikköympyrän sisälle osuvien pisteiden määrä
# jos pisteen koordinaatit toteuttavat epäyhtälön x^2+y^2<1, piste on ympyrässä
import random

#TODO: kysy N arvo käyttäjältä
N = 100 # pisteiden kokonaismäärä
n = 0 # ympyrään osuvien pisteiden lkm
iterator = 0
while iterator < N:
    iterator += 1
    # arvotaan yksi piste
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print(f"Arvottu piste: {x}, {y}")
    #print(x**2 + y**2 < 1)
    if x**2 + y**2 < 1:
        print("Piste on yksikköympyrässä.")
        #TODO: lisää n arvoon 1
#TODO: tulosta kaavan mukaan laskettu piin likiarvo
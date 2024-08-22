# Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.
# pii*r^2
import math

r = float(input("Anna ympyrän säde (m): "))
area = math.pi * r * r
print(f"Ympyrän, jonka säde on {r}, pinta-ala on {area:.1f} neliömetriä.")

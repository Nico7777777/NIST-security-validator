import numpy as np
from scipy.special import gammainc
import math
import sys  # ma ajuta sa imi opresc fortat programul.

#Ipoteza de nul 0 H : secvența binară generată este (pseudo)aleatoare.
#Ipoteza alternativă A H : secvența binară generată nu este (pseudo)aleatoare.
def check_len(v, n):
  if len(v) < n:
    print("Nu ati citit secventa de lungimea corecta")
    return 1
  return 0

def check_m(m, n):
  if m > (math.log2(n) - 2):
    print("Numarul m nu indeplineste conditia obligatorie!")
    return 1
  return 0

def build_secv(v, m):
    n = len(v)
    secvente = []
    for i in range(1, 4):
        if m - i > 0:
          new_secv = v + v[0:m-i]
          secvente.append(new_secv)
        elif m - i == 0:
          new_secv  = v
          secvente.append(new_secv)
        else:
          break
    return secvente

def found_pattern(v, m):
   n = len(v)
   pattern_dictionary  = {}
   # preiau toate patternurile de lungime m
   # si le adaug intr un dictionar
   for i in range(n - m + 1):
      pattern = tuple(v[i:i+m])
      if pattern in pattern_dictionary:
        pattern_dictionary[pattern] +=1
        # cresc frecventa pattern-ului respectiv in dictionar, adica cresc valoarea cheii.
      else:
        pattern_dictionary[pattern] = 1

   # cheile sunt patternurile, valorile sunt count-urile asociate cu pattern-urile.
   # .items() genereaza perechea de iteratori (cheie, valoare)
   found_patterns = {pattern: count for pattern, count in pattern_dictionary.items() if count > 1}
   return found_patterns


print("Introduceti lungimea dorita a secventei de biti:")
n = int(input())
n_str = str(n)
print("Introduceti secventa de " + n_str + " biti:")
arr = input()
v = list(map(int, arr.split(' ')))
# aici imi preia toata linia in care citesc elementele
# pe care le citesc separate printr-un spatiu, si apoi la mapez in inturi
# in cadrul vectorului
if check_len(v, n) == 1:
  sys.exit()  # in caz ca nu am citit corect v, se iese fortat.

print("Introduceti nivelul de semnificatie alfa:")
alfa = float(input())

print("Introduceti lungimea dorita a pattern-urilor de verificat, m: ")
m = int(input())
if check_m(m, n) == 1:
  sys.exit()

secvente = build_secv(v, m)

m_new = m
# initializez cele 3 functii pe care le vom volosi la calculul functiilor de test.
funcm = 0
funcm_1 = 0
funcm_2 = 0
functii = [0] * (3)
ct = 0

for i, secventa in enumerate(secvente):
    sum = 0  # calculam suma frecventelor ridicate la patrat
    # print(f"s_{i+1}: {secventa}")
    found_patterns = found_pattern(secventa, m_new)
    # print(found_patterns)
    for pattern, frecventa in found_patterns.items():
      # afisez cheie + valoarea aferenta, => itemii
      print(f"Pattern: {pattern}, frecventa: {frecventa}")
      sum = sum + math.pow(frecventa, 2)
      functii[ct] = ((math.pow(2, m_new))/n) * sum - n
    print(functii[ct])
    print("\n")
    m_new = m_new - 1
    ct = ct + 1
for i in range(0, 3):
  print(functii[i])
  # daca nu am populat un element al vectorului de functii, automat l-am pus pe 0
  # din atribuirile initiale [0] * 3
statistica_1 = 0
statistica_2 = 0
statistica_1 = functii[0] - functii[1]
statistica_2 = functii[0] - 2 * functii[1] + functii[2]

p_value1 = gammainc(math.pow(2, m - 2), statistica_1/2)
p_value2 = gammainc(math.pow(2, m - 3), statistica_2/2)
print(statistica_1)
print(statistica_2)
print(p_value1)
print(p_value2)
# daca se indeplinesc cele doua conditii, rezulta ca ipoteza de nul se accepta,
# in caz contrar nu.
if p_value1 > alfa and p_value2 > alfa:
  print("Se accepta ipoteza de nul la nivelul de semnificatie primit ca intrare de " + str(alfa))
else:
  print("Nu se accepta ipoteza de nul la nivelul de semnificatie primit ca intrare de " + str(alfa))

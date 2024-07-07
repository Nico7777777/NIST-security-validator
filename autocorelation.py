import math
import sys  
# ma ajuta sa imi opresc fortat programul.

# Ipoteza de nul 0 H : secvența binară generată este (pseudo)aleatoare.
# Ipoteza alternativă A H : secvența binară generată nu este (pseudo)aleatoare.
def check_len(v, n):
  if len(v) < n:
    print("Nu ati citit secventa de lungimea corecta")
    return 1
  return 0

def check_interval(x, y):
  if not(x >= 1 and x <= y and y <= n//2):
    print("Formatul intervalului nu este unul corect")
    return 1
  return 0

print("Introduceti lungimea dorita a secventei de biti:")
n = int(input())
n_str = str(n)
print("Introduceti secventa de " + n_str + " biti:")
arr = input()  
# aici imi preia toata linia in care citesc elementele
# pe care le citesc separate printr-un spatiu, si apoi la mapez in inturi 
# in cadrul vectorului
v = list(map(int, arr.split(' ')))  
if check_len(v, n) == 1:
  sys.exit()  # in caz ca nu am citit corect v, se iese fortat.

print("Introduceti nivelul de semnificatie alfa:")
alfa = float(input())

x, y = map(int, input("Introduceti un interval valid de numere naturale. Capatul din stanga trebuie sa fie mai mare ca 1, iar cel din dreapta mai mic ca n/2\n ").split())
if check_interval(x, y) == 1:
  sys.exit()
# printez si intervalul
print("Capatul din stanga:", x)
print("Capatul din dreapta:", y)
ok = 1
for d in range(x, y + 1, 1):
  # d va fi lungimea shiftului la stanga
  new_secv = [0] * (n - d)
  sum = 0
  # in vectorul new_secv voi memora secventa prelucrata cu operatorul xor.
  for i in range(len(new_secv)):
    new_secv[i] = v[i] ^ v[i + d] 
    # am aplicat xor intre bitii aferenti.
    new_secv[i] = 2 * new_secv[i] - 1
    # am transformat bitii de 0 in -1, iar cei de 1 au ramas 1.
    sum = sum + new_secv[i]
  sum_abs = abs(sum)
  print(sum_abs)
  sum_abs = sum_abs / math.sqrt(n - d)
  p_value = math.erfc(sum_abs / math.sqrt(2))
  print(p_value)
  if p_value < alfa:
    print("Nu se accepta ipoteza de nul la nivelul de semnificatie primit ca intrare de " + str(alfa))
    ok = 0
    break

# daca nu se iese din bucla for cu break, fortat, ipoteza de nul se accepta,
# in caz contrar, nu se executa urmatoarele doua linii, ipoteza deja fiind analizata
# si ajungand la concluzia ca nu se accepta pentru ca nu se indeplineste conditia.
if ok == 1:
  print("Se accepta ipoteza de nul la nivelul de semnificatie primit ca intrare de " + str(alfa))
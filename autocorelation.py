import math
import sys  # helps me forcibly stop my program.

# Null hypothesis H0: The generated binary sequence is (pseudo)random.
# Alternative hypothesis H1: The generated binary sequence is not (pseudo)random.
def check_len(v, n):
  if len(v) < n:
    print("You did not enter a sequence of the correct length")
    return 1
  return 0

def check_interval(x, y):
  if not(x >= 1 and x <= y and y <= n//2):
    print("The interval format is not correct")
    return 1
  return 0

print("Enter the desired length of the bit sequence:")
n = int(input())
n_str = str(n)
print("Enter the sequence of " + n_str + " bits:")
arr = input()  
# Here it takes the entire line in which I read the elements
# which I read separated by a space, and then map them to integers 
# in the vector
v = list(map(int, arr.split(' ')))  
if check_len(v, n) == 1:
  sys.exit()  # If the input v is not correct, exit forcibly.

print("Enter the significance level alpha:")
alpha = float(input())

x, y = map(int, input("Enter a valid interval of natural numbers. The left end must be greater than 1, and the right end less than n/2\n ").split())
if check_interval(x, y) == 1:
  sys.exit()
# Print the interval
print("Left end:", x)
print("Right end:", y)
ok = 1
for d in range(x, y + 1, 1):
  # d will be the length of the left shift
  new_secv = [0] * (n - d)
  sum = 0
  # In the vector new_secv I will store the sequence processed with the xor operator.
  for i in range(len(new_secv)):
    new_secv[i] = v[i] ^ v[i + d] 
    # Applied xor between the corresponding bits.
    new_secv[i] = 2 * new_secv[i] - 1
    # Converted the bits from 0 to -1, while the 1 bits remained 1.
    sum = sum + new_secv[i]
  sum_abs = abs(sum)
  print(sum_abs)
  sum_abs = sum_abs / math.sqrt(n - d)
  # In sum_abs I  will score the test statistic
  p_value = math.erfc(sum_abs / math.sqrt(2))
  print(p_value)
  if p_value < alpha:
    print("The null hypothesis is not accepted at the significance level provided: " + str(alpha))
    ok = 0
    break

# If the for loop does not exit with a forced break, the null hypothesis is accepted,
# otherwise, the following two lines are not executed, the hypothesis has already been analyzed
# and it was concluded that it is not accepted because the condition was not met.
if ok == 1:
  print("The null hypothesis is accepted at the significance level provided: " + str(alpha))
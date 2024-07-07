import numpy as np
from scipy.special import gammainc
import math
import sys  # helps me forcibly stop my program.


# Null hypothesis H0: The generated binary sequence is (pseudo)random.
# Alternative hypothesis H1: The generated binary sequence is not (pseudo)random.
def check_len(v, _n: int) -> bool:
    if len(v) < _n:
        print("You did not enter a sequence of the correct length")
        return False
    return True


def check_m(_m: int, _n: int) -> bool:
    if _m > (math.log2(_n) - 2):
        print("The number m does not meet the mandatory condition!")
        return False
    return True


def build_secv(_v, _m: int) -> list[int]:
    seqs = []
    for _i in range(1, 4):
        if _m - _i > 0:
            new_secv = _v + _v[0:_m - _i]
            seqs.append(new_secv)
        elif _m - _i == 0:
            new_secv = _v
            seqs.append(new_secv)
        else:
            break
    return seqs


def found_pattern(v, m):
    n = len(v)
    pattern_dictionary = {}
    # Take all patterns of length m and add them to a dictionary
    for i in range(n - m + 1):
        pattern = tuple(v[i:i + m])
        if pattern in pattern_dictionary:
            pattern_dictionary[pattern] += 1
            # Increase the frequency of the pattern in the dictionary, i.e., increase the key's value.
        else:
            pattern_dictionary[pattern] = 1

    # The keys are the patterns, the values are the counts associated with the patterns.
    # .items() generates the pair of iterators (key, value)
    found_patterns = {pattern: count for pattern, count in pattern_dictionary.items() if count > 1}
    return found_patterns


print("Enter the desired length of the bit sequence:")
n = int(input())
n_str = str(n)
print("Enter the sequence of " + n_str + " bits:")
arr = input()
v = list(map(int, arr.split(' ')))
# Here it takes the entire line in which I read the elements
# which I read separated by a space, and then map them to integers
# in the vector
if not check_len(v, n):
    sys.exit()  # If the input v is not correct, exit forcibly.

print("Enter the significance level alpha:")
alpha = float(input())

print("Enter the desired length of the patterns to check, m: ")
m = int(input())
if not check_m(m, n):
    sys.exit()

sequences = build_secv(v, m)

m_new = m
# Initialize the 3 functions that we will use to calculate the test functions.
funcm = 0
funcm_1 = 0
funcm_2 = 0
functions = [0] * (3)
ct = 0

for i, sequence in enumerate(sequences):
    sum = 0  # Calculate the sum of squared frequencies
    # print(f"s_{i+1}: {sequence}")
    found_patterns = found_pattern(sequence, m_new)
    # print(found_patterns)
    for pattern, frequency in found_patterns.items():
        # Display the key + its value => items
        print(f"Pattern: {pattern}, frequency: {frequency}")
        sum = sum + math.pow(frequency, 2)
        functions[ct] = ((math.pow(2, m_new)) / n) * sum - n
    print(functions[ct])
    print("\n")
    m_new = m_new - 1
    ct = ct + 1
for i in range(0, 3):
    print(functions[i])
    # If an element of the functions vector is not populated, it was set to 0 by the initial assignments [0] * 3
statistic_1 = 0
statistic_2 = 0
statistic_1 = functions[0] - functions[1]
statistic_2 = functions[0] - 2 * functions[1] + functions[2]

p_value1 = gammainc(math.pow(2, m - 2), statistic_1 / 2)
p_value2 = gammainc(math.pow(2, m - 3), statistic_2 / 2)
print(statistic_1)
print(statistic_2)
print(p_value1)
print(p_value2)
# If both conditions are met, the null hypothesis is accepted,
# otherwise it is not.
if p_value1 > alpha and p_value2 > alpha:
    print("The null hypothesis is accepted at the significance level provided: " + str(alpha))
else:
    print("The null hypothesis is not accepted at the significance level provided: " + str(alpha))

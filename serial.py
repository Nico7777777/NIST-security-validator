from typing import List
from scipy.special import gammainc
from math import pow, log2


# Null hypothesis H0: The generated binary sequence is (pseudo)random.
# Alternative hypothesis H1: The generated binary sequence is not (pseudo)random.

def check_len(v: bytes, _n: int) -> bool:
    if len(v) < _n:
        print("You did not enter a sequence of the correct length")
        return False
    return True


def check_m(_m: int, _n: int) -> bool:
    if _m > (log2(_n) - 2):
        print("The number m does not meet the mandatory condition!")
        return False
    return True


def build_secv(_v: bytes, _m: int) -> List[bytes]:
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


def serial(n: int, arr: str, alpha: float, m: int) -> str:
    v = list(int(bit) for bit in arr)
    if not check_len(bytes(v), n):
        return "Invalid sequence length."

    if not check_m(m, n):
        return "Invalid value for m."

    sequences = build_secv(bytes(v), m)

    m_new = m
    # Initialize the 3 functions that we will use to calculate the test functions.
    functions = [0] * 3
    result = ""

    ct = 0
    for i, sequence in enumerate(sequences):
        _sum = 0  # Calculate the sum of squared frequencies
        result += f"s_{i + 1}: {sequence}\n"
        found_patterns = found_pattern(sequence, m_new)
        # print(found_patterns)
        for pattern, frequency in found_patterns.items():
            # Display the key + its value => items
            result += f"Pattern: {pattern}, frequency: {frequency}\n"
            _sum = _sum + pow(frequency, 2)
            functions[ct] = ((pow(2, m_new)) / n) * _sum - n
        m_new = m_new - 1
        ct = ct + 1

    for i in range(0, 3):
        result += f"{functions[i]}\n"
        # If an element of the functions vector is not populated, it was set to 0 by the initial assignments [0] * 3
    statistic_1 = functions[0] - functions[1]
    statistic_2 = functions[0] - 2 * functions[1] + functions[2]

    p_value1 = gammainc(pow(2, m - 2), statistic_1 / 2)
    p_value2 = gammainc(pow(2, m - 3), statistic_2 / 2)

    result += f"Statistic 1: {statistic_1}, p-value 1: {p_value1}\n"
    result += f"Statistic 2: {statistic_2}, p-value 2: {p_value2}\n"

    # If both conditions are met, the null hypothesis is accepted,
    # otherwise it is not.
    if p_value1 > alpha and p_value2 > alpha:
        result += "The null hypothesis is accepted at the significance level provided."
    else:
        result += "The null hypothesis is not accepted at the significance level provided."
    return result

# Only for testing purposes
# if __name__ == '__main__':
#     k = serial(30, "101101001010011011101001110011", 0.01, 3)
#     print(k)

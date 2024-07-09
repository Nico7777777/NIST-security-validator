import math


# Null hypothesis H0: The generated binary sequence is (pseudo)random.
# Alternative hypothesis H1: The generated binary sequence is not (pseudo)random.

def check_len(_v: bytes, _n: int) -> bool:
    if len(_v) < _n:
        print("You did not enter a sequence of the correct length")
        return False
    return True


def check_interval(_x: int, _y: int, _n: int) -> bool:
    if not (1 <= _x <= _y <= _n // 2):
        print("The interval format is not correct")
        return False
    return True


def autocorrelation(n, arr, alpha, x, y):
    v = list(int(bit) for bit in arr)
    if not check_len(bytes(v), n):
        return "Sequence length is not correct"

    if not check_interval(x, y, n):
        return "Interval is not correct"

    result = ""
    ok = 1
    for d in range(x, y + 1):
        # d will be the length of the left shift
        new_secv = [0] * (n - d)
        sum = 0
        # In the vector new_secv I will store the sequence processed with the xor operator
        for i in range(len(new_secv)):
            new_secv[i] = v[i] ^ v[i + d]
            # Applied xor between the corresponding bits.
            new_secv[i] = 2 * new_secv[i] - 1
            # Converted the bits from 0 to -1, while the 1 bit remained 1.
            sum = sum + new_secv[i]
        sum_abs = abs(sum)
        sum_abs = sum_abs / math.sqrt(n - d)
        # In sum_abs I  will score the test statistic
        p_value = math.erfc(sum_abs / math.sqrt(2))
        result += f"Calculated p_value is: {p_value}\n"
        if p_value < alpha:
            result += f"The null hypothesis is not accepted at the significance level {alpha}\n"
            ok = 0
            break

    # If the for loop does not exit with a forced break, the null hypothesis is accepted,
    # otherwise, the following two lines are not executed, the hypothesis has already been analyzed,
    # and it was concluded that it is not accepted because the condition was not met.
    if ok == 1:
        result += f"The null hypothesis is accepted at the significance level {alpha}\n"

    return result

# Only for testing purposes
# if __name__ == '__main__':
#     k = autocorrelation(30, "101101001010011011101001110011", 0.01, 6, 6)
#     print(k)

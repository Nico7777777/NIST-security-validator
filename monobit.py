import math
import scipy


def monoBit(alpha, token):
    # H0: p = 0.5 (null hypothesis)
    # HA: p != 0.5 (alternative hypothesis)

    # Length of string (token)
    length = len(token)
    # number of '1' in the string
    n1 = 0

    # Counting '1's
    for i in range(length):
        if token[i] == '1':
            n1 = n1 + 1

    # Compute '0's
    n0 = length - n1

    # Test Function
    f = abs(n1 - n0) / math.sqrt(length)

    # Compute one quantile
    z = scipy.stats.norm.ppf(alpha / 2)

    # Test - Acceptance Region
    if z <= f <= -z:
        return f"The sequence is pseudo-random -> f = {str(round(f, 4))} belongs to the region [{str(round(z, 4))}, {str(round(-z, 4))}]"
    return f"The sequence is not pseudo-random"


if __name__ == '__main__':
    k = monoBit(0.01, "101101001010011011101001110011")
    print(k)

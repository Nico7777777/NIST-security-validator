from monobit import monoBit
import scipy


def mBit(alpha: float, m: int, token: bytes) -> str:  # returneaza un mesaj de eroare/succes catre terminal
    # Monobit Test
    if m == 1:
        return monoBit(alpha, token)

    # The length of the Token
    length = len(token)

    # Test NIST Recommendation
    if m <= 0.1 * length:
        print("NIST recommendation is not fulfilled - Block Size Test")

    # Get number of blocks
    blocksNum = length // m

    # Create an empty array
    p = [0] * blocksNum

    # Count the ones
    for i in range(blocksNum):
        c = 0
        for j in range(m):
            if token[i * m + j] == '1':
                c = c + 1
        p[i] = c

    # Compute Squared Sum
    s = 0
    for i in range(blocksNum):
        s = s + (p[i] - 0.5) ** 2

    # Compute the Test Function
    chiFunction = 4 * m * s

    # Compute the Degrees of Freedom
    degree = 2 ** m - 1

    # Compute the Acceptance Region
    chiAlpha0 = scipy.stats.chi2.ppf(alpha / 2, degree)
    chiAlpha1 = scipy.stats.chi2.ppf(1 - alpha / 2, degree)

    # Test - Acceptance Region
    if chiAlpha0 <= chiFunction <= chiAlpha1:
        return f"The sequence is pseudo-random -> f = {str(round(chiFunction, 4))} belongs to the region [{str(round(chiAlpha0, 4))}, {str(round(chiAlpha1, 4))}]"
    return f"The sequence is not pseudo-random"

# Only for testing purposes
# if __name__ == '__main__':
#     k = mBit(0.01, 4, bytes(list(int(i) for i in "101101001010011011101001110011")))
#     print(k)

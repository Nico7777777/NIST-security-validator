import math

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
        return "Error: Sequence length is not correct"
    
    if not check_interval(x, y, n):
        return "Error: Interval is not correct"

    result = ""
    ok = 1
    for d in range(x, y + 1):
        new_secv = [0] * (n - d)
        sum = 0
        for i in range(len(new_secv)):
            new_secv[i] = v[i] ^ v[i + d]
            new_secv[i] = 2 * new_secv[i] - 1
            sum = sum + new_secv[i]
        sum_abs = abs(sum)
        sum_abs = sum_abs / math.sqrt(n - d)
        p_value = math.erfc(sum_abs / math.sqrt(2))
        result += f"Calculated p_value is: {p_value}\n"
        if p_value < alpha:
            result += f"The null hypothesis is not accepted at the significance level {alpha}\n"
            ok = 0
            break

    if ok == 1:
        result += f"The null hypothesis is accepted at the significance level {alpha}\n"
    
    return result

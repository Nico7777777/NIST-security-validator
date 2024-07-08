# NIST-security-validator
this project was made during the MATH4ENG summer school, an EELISA project of University Politehnica of Bucharest 

In this project, we aimed to implement several statistical tests of (pseudo) randomness to determine if a given (generated) binary sequence can be considered random. The practical utility of our project would be in testing the quality of pseudorandom number generators, with the results of the implemented tests being probabilistic. The four algorithms we chose for implementation, in accordance with the requirements of the National Institute of Standards and Technology (NIST), are as follows:

1. Frequency (Monobit) Test
2. Frequency Test within a Block (M-bit test)
3. Autocorrelation Test
4. Serial Test

# Description of the functionality of the four tests:

# Frequency (Monobit) Test:

The focus of the test is the proportion of zeroes and ones for the entire sequence. The purpose of this test is to determine whether the number of ones and zeros in a sequence are approximately the same as would be expected for a truly random sequence. Subsequent tests depend on the passing of this test.

# Frequency Test within a Block (M-bit test):

The focus of the test is the proportion of ones within M-bit blocks. The purpose of this test is to determine whether the frequency of ones in an M-bit block is approximately M/2, as would be expected under an assumption of randomness. For block size M=1, this test degenerates to the Frequency (Monobit) test.

# Autocorrelation Test:

The purpose of this test is to determine possible correlations within a sequence of n bits (non-cyclic) and its shifted version. For the sequence to be truly random, it should be independent of a new sequence obtained by a logical shift (to the left) of a given length (called the autocorrelation distance), so the degree of correlation of the generated sequence should be very small, as close to 0 as possible.

A brief description of the used functions:

## check_len:
The function receives as arguments a vector of bytes and its length, an integer, and checks if a valid sequence has been entered, if the length of the read vector matches the number n.

## check_interval:
The function receives as arguments 3 integers x, y, and n, and has the role of checking that 1 <= x <= y <= [n/2], where y will be associated with d, the length of the shift. The user thus has the possibility to enter an interval for the length of the shift from which the algorithm will extract natural numbers, for greater precision of the autocorrelation test, as it is recommended to check the sequence with as many shift lengths as possible.

## autocorrelation():
User-entered data is read: the length of the bit sequence, the corresponding sequence, the significance level alpha, and the ends of the interval from which the length for the shift, d, will be extracted. In a repetitive for loop, I will iterate through the initial bit sequence and extract into a vector, new_secv, the values obtained by the xor operation between the elements at position i and (i + d), for i from 0 to (n-d-1), and this sum will represent the number of bits in sequence n s that differ from the bits in the shifted version. With the help of this sum, I calculate the test statistic, then check if the p_value, i.e., the probability of making a Type I error (rejecting the null hypothesis H0, although it is true), which is then compared to the significance level (the maximum probability with which the null hypothesis H0 is rejected).

# Serial Test:

The focus of this test is the frequency of all possible overlapping m-bit patterns across the entire sequence. The purpose of this test is to determine whether the number of occurrences of the 2^m m-bit overlapping patterns is approximately the same as would be expected for a random sequence. Truly random sequences belong to the uniform distribution, so the appearance of a certain pattern of "m" bits is equally probable. For m = 1, the Serial test is equivalent to the Frequency test.
Serial Test:

A brief description of the used functions:

## check_len(v, n):
This function checks if the elements of the sequence being analyzed are exactly n in number.

## check_m(m, n):
This function checks if m satisfies the condition of being less than or equal to the logarithm base 2 of n, all minus 2, a condition required for the algorithm to function properly.

## build_secv(v, m): 
In this function, we construct the 3 test sequences, where at the end of the initial sequence, if they exist, the first m-1 bits, m-2 bits, and m-3 bits are appended, respectively. For i from 1 to 3 inclusive, if m - i is positive, the respective bits are appended at the end; otherwise, if m - i is equal to 0, the initial sequence is returned, and in any other case, an empty list is returned.

## found_pattern(v, m):
This function helps to determine each pattern within a sequence, with its relative frequency, i.e., how many times that pattern of length m appears within the entire sequence. I used a dictionary where I sequentially introduced each pattern of length m, iterating through the vector from position 0 to n - m + 1. I then incremented the frequency of the found pattern if it already existed in the dictionary; otherwise, I assigned it a frequency of 1. This function returns all found patterns and their associated frequencies as key-value pairs.

## serial():

Everything begins by reading the length of the sequence n, the bit sequence, the significance level alpha, and the pattern length m from the keyboard, verifying all necessary conditions. I iterate through the list of sequences, call the found_pattern function, whose result (the dictionary) I store in found_patterns. Then, iterating through the obtained dictionary for each test sequence, I calculate the sum of the squared frequencies, which I then use in the calculation formula for the three functions. Additionally, I calculate the two test statistics and use the incomplete gamma function to determine the acceptance region of the null hypothesis.

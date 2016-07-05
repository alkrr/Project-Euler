"""
Project Euler Problem 1:
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

Answer: 233168.0
"""

"""
Int, Int -> Float
Takes a limit n and a value mul as input, returns the sum of all multiples of mul
in range [0, n]

Call gp_sum in following way:

>> gp_sum(999, 3) + gp_sum(999, 5) - gp_sum(999, 15)
>> (output) 
233168.0
"""

def gp_sum(n, mul):
    if mul == 1:         # edge case to avoid division by 0
        return n
    number_terms = n / mul
    last_term = mul * number_terms
    first_term = mul
    sum2 = 0.5 * (first_term + last_term) * number_terms 
    return sum

# gives off by one error    
def gp_sum_1(n, mul):
    if mul == 1:         # edge case to avoid division by 0
        return n
    number_terms = n / mul
    last_term = mul * number_terms
    first_term = mul
    sum = (first_term + last_term) * (number_terms / 2)     #off by one error
    return sum
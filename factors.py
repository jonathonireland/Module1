# is number even or odd?
def check_even_odd(factors):
    even_odd = {}
    for factor in factors:
        if factor % 2 == 0:
            even_odd[factor] = 'Even'
        else:
            even_odd[factor] = 'Odd'
    return even_odd

# Return array of factors to print
def find_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

# Input from the user
num = int(input("Get the factors of a number: "))

# Find factors
factors = find_factors(num)

# Check if factors are even or odd
even_odd_factors = check_even_odd(factors)

# Display each factor and parity (oddness or evenness)
for factor, parity in even_odd_factors.items():
    print(f"Factor: {factor}, {parity}")
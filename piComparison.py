from decimal import Decimal, getcontext

# Set precision high enough for 100 decimal places
getcontext().prec = 110

def leibniz_pi(terms):
    pi = Decimal(0)
    for k in range(terms):
        term = Decimal((-1) ** k) / Decimal(2 * k + 1)
        pi += term
    return pi * Decimal(4)

# Compute pi using many terms
pi_value = leibniz_pi(200000)

# Baseline approximations
pi_1415 = Decimal("3.1415")
pi_1416 = Decimal("3.1416")

# Decimal places to compare
places = [20, 40, 60, 100]

print("Computed π:\n")
for p in places:
    getcontext().prec = p + 5
    print(f"{p} decimal places:")
    print(str(pi_value)[:p + 2])
    print()

# Reset precision for error comparison
getcontext().prec = 30

print("Error comparison:\n")
print("Error of 3.1415 =", pi_1415 - pi_value)
print("Error of 3.1416 =", pi_1416 - pi_value)

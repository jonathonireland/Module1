def is_all_digits_even(num):
    while num > 0:
        digit = num % 10
        if digit % 2 != 0:
            return False
        num //= 10
    return True

even_digit_numbers = []

for num in range(1000, 3001):
    if is_all_digits_even(num):
        even_digit_numbers.append(str(num))

print("Numbers with all even digits between 1000 and 3000 (inclusive):")
print(", ".join(even_digit_numbers))
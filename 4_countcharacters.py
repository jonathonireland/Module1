def count_letters_and_digits(input_string):
    letters = 0
    digits = 0
    for char in input_string:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
    return letters, digits

# Input from the user
input_string = input("Enter a sentence: ")

# Count letters and digits
letters, digits = count_letters_and_digits(input_string)

# Print the results
print(f"LETTERS: {letters}")
print(f"DIGITS: {digits}")
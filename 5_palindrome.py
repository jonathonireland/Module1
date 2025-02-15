def is_palindrome(number):
    # Convert the number to a string
    number_str = str(number)
    # Check if the string is equal to its reverse
    return number_str == number_str[::-1]

# Input from the user
number = int(input("Enter a number: "))

# Check if the number is a palindrome
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
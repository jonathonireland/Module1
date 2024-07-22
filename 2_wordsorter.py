# Function to sort words alphabetically
def sort_words(words):
    return sorted(words)

# Input from the user
input_words = input("Enter a sequence of words separated by spaces: ")

# Split the input string into words
words = input_words.split()

# Sort the words
sorted_words = sort_words(words)

# Print the sorted words
print("Sorted words:")
for word in sorted_words:
    print(word)
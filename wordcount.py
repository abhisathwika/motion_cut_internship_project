def get_user_input():
    text = input("Please enter a sentence or paragraph: ")
    return text
def count_words(text):
    # Split the text into words using spaces as delimiters
    words = text.split()
    # Count the number of words in the list
    return len(words)
def word_counter():
    # Get input from the user
    text = get_user_input()
    
    # Check for empty input
    if not text.strip():
        print("Error: You did not enter any text. Please try again.")
        return
    
    # Count the words and display the result
    word_count = count_words(text)
    print(f"The number of words in the text is: {word_count}")
# Function to prompt the user for input
def get_user_input():
    text = input("Please enter a sentence or paragraph: ")
    return text

# Function to count the number of words in a given text
def count_words(text):
    # Split the text into words using spaces as delimiters
    words = text.split()
    # Count the number of words in the list
    return len(words)

# Main function to execute the word counter program
def word_counter():
    # Get input from the user
    text = get_user_input()
    
    # Check for empty input
    if not text.strip():
        print("Error: You did not enter any text. Please try again.")
        return
    
    # Count the words and display the result
    word_count = count_words(text)
    print(f"The number of words in the text is: {word_count}")

# Run the program
if __name__ == "__main__":
    word_counter()

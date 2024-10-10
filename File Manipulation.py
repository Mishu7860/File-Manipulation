def count_word_occurrences(filename):
    # Initialize a dictionary to store word counts
    word_count = {}

    try:
        # Open the file for reading
        with open(filename, 'r', encoding='utf-8') as file:
            # Read the contents of the file
            text = file.read()

            # Split the text into words
            words = text.split()

            # Count occurrences of each word
            for word in words:
                # Remove punctuation and convert to lowercase
                cleaned_word = ''.join(char for char in word if char.isalnum()).lower()
                if cleaned_word:  # Ensure the word is not empty
                    if cleaned_word in word_count:
                        word_count[cleaned_word] += 1
                    else:
                        word_count[cleaned_word] = 1

        # Sort the words alphabetically
        sorted_word_count = dict(sorted(word_count.items()))

        # Display the results
        print("Word occurrences:")
        for word, count in sorted_word_count.items():
            print(f"{word}: {count}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
file_name = input("Enter the filename (with .txt extension) to count word occurrences: ")
count_word_occurrences(file_name)

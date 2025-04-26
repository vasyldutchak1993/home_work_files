"""
You have a text file. Count how many times the word
specified by the user occurs in it.
"""
FILE = "../storage/task_5.txt"

def count_words(filepath,word_to_count=''):
    try:
        with open(filepath, "r") as file:
            result = {
                word_to_count:0
            }
            for line in file:
                if word_to_count in line:
                    result[word_to_count] += 1
            return result
    except FileNotFoundError:
        print(f"File not found {filepath}")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")


print(count_words(FILE,"you"))
"""
You have a text file. Create a new file and write the following statistics based on the source file to it:
■ Number of characters;
■ Number of lines;
■ Number of vowels;
■ Number of consonants;
■ Number of digits.
"""
from functools import reduce

FILE_TO_ANALYZE = "../storage/task_2.txt"
STATISTICS_FILE="../storage/task_2_temp.txt"

"""
similar func  to easy to understand 

def count_digits(text):
    return reduce(lambda count, char: count + 1 if char.isdigit() else count, text, 0)
"""
def count_digits_(text):
    result = 0
    for char in text:
        if char.isdigit():
            result += 1
    return result


def count_digits(text):
    return reduce(lambda count, char: count + 1 if char.isdigit() else count, text, 0)

def count_consonants_and_vowels(text):
    vowels = "aeiouAEIOU"
    consonant_count = 0
    vowels_count = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            consonant_count += 1
        elif char in vowels:
            vowels_count += 1
    return consonant_count,vowels_count


def generate_statistics(file_to_analyze, statistics_file=STATISTICS_FILE):
    try:
        with open(file_to_analyze, "r") as file:
            statistics = {
                "characters_count": 0,
                "lines_count": 0,
                "vowels_count": 0,
                "consonants_count": 0,
                "digits_count": 0
            }
            for line in file:
                normalized_line = line.strip()
                consonants_count, vowels_count = count_consonants_and_vowels(normalized_line)
                statistics["lines_count"] += 1
                statistics["characters_count"] += len(normalized_line)
                statistics["vowels_count"] += vowels_count
                statistics["consonants_count"] += consonants_count
                statistics["digits_count"] += count_digits(normalized_line)
        with open(statistics_file, "w") as stat_file:
            stat_file.write(str(statistics))
    except FileNotFoundError :
        print(f"Error: {file_to_analyze} not found.")
    except PermissionError:
        print(f"Error: Permission denied while trying to write to {stat_file}.")
    except IOError:
        print(f"Error: An unexpected I/O error occurred while writing to {stat_file}.")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")


generate_statistics(FILE_TO_ANALYZE)

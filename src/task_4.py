"""
You have a text file. Find the length of the longest line
"""
from functools import reduce

FILE = "../storage/task_4.txt"


def find_longest_line(filepath):
    try:
        with open(filepath, "r") as file:
            lines = file.readlines()

            if not lines:
                return "FILE IS EMPTY"

            longest_line = lines[0]

            for line in lines:
                if len(line) > len(longest_line):
                    longest_line = line

            return longest_line

    except FileNotFoundError:
        print(f"File not found {filepath}")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")


print(find_longest_line(FILE))
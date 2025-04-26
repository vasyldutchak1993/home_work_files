"""
You have a text file. Find and replace the specified word.
The user determines what to search for and to what it should
be replaced.
"""

FILE = "../storage/task_6.txt"

def replace_word(filepath,search_word,replace_word):
    try:
        with open(filepath, "r+") as file:
            data = file.readlines()
            for idx,line in enumerate(data):
                data[idx] = line.replace(search_word,replace_word)
            file.seek(0)
            file.writelines(data)
            file.truncate()
    except FileNotFoundError:
        print(f"File not found {filepath}")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")


replace_word(FILE,"you","YOU BRO")
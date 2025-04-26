"""
You have a text file. Delete the last line from it. Write
the result to another file
"""
FILE = "../storage/task_3.txt"
FILE_TO_SAVE="../storage/task_3_copy.txt"

def copy_without_last_line(file_to_read,file_to_save=FILE_TO_SAVE):
    try:
        with open(file_to_read, "r") as file_origin:
            data= "".join(file_origin.readlines()[:-1])
        with open(file_to_save, "w") as file:
            file.write(data)
    except FileNotFoundError:
        print(f"File not found {file_to_save}")
    except PermissionError:
        print(f"Error: Permission denied while trying to write to {file_to_read}.")
    except IOError:
        print(f"Error: An unexpected I/O error occurred while writing to {file_to_read}.")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")


copy_without_last_line(FILE)

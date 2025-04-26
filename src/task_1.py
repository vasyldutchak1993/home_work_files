"""
You have two text files. Find out if their lines match. If
they don’t, print the mismatched line from each file.
"""
FILE_1_PATH = "../storage/task_1_1_text.txt"
FILE_2_PATH = "../storage/task_1_text.txt"


def compare_files(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            first_file_line = f1.readline()
            second_file_line = f2.readline()
            while first_file_line and second_file_line:
                if first_file_line != second_file_line:
                    print(first_file_line.strip(),"<------->",second_file_line.strip())
                first_file_line=f1.readline()
                second_file_line=f2.readline()
    except FileNotFoundError as error:
        print(error)


compare_files(FILE_1_PATH, FILE_2_PATH)

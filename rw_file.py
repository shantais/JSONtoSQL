import json
import os

def load_journals():
    file_name = "journals_data.json"

    if os.path.exists(file_name):
        # read existing file and update new data
        with open(file_name, mode="r", encoding="utf-8") as f:
            journals_loaded_dict = json.load(f)
    else:
        journals_loaded_dict = {}

    return journals_loaded_dict


def add(sql_line, file_name):
    data_file = "data.txt"
    if os.path.exists(data_file):
        with open(data_file, mode="a", encoding="utf-8") as f:
            f.write("\n" + sql_line)
    else:
        with open(data_file, mode="w", encoding="utf-8") as f:
            f.write(sql_line)

    if os.path.exists(file_name):
        with open(file_name, mode="a", encoding="utf-8") as f:
            f.write("\n" + sql_line)
    else:
        with open(file_name, mode="w", encoding="utf-8") as f:
            f.write(sql_line)


def read(file_name, sql_author_line):
    author_id = 0
    line_number = 0
    if os.path.exists(file_name):
        with open(file_name, mode="r", encoding="utf-8") as f:
            for idx, line in enumerate(f):
                line_number = idx + 1
                if line.strip() == sql_author_line:
                    author_id = idx + 1
                    break
    return author_id, line_number
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
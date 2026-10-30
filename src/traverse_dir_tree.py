from pathlib import Path
import pprint
import os


# returns a list of strings of files' full paths


def traverse_dir_tree(root_dir: str) -> list[str]:

    file_full_path_list = []

    for filename in os.listdir(root_dir):
        full_path = os.path.join(root_dir, filename)
        # file_size = os.path.getsize(full_path)
        if os.path.isfile(full_path):
            file_full_path_list.append(full_path)
        elif os.path.isdir(full_path):
            file_full_path_list.extend(traverse_dir_tree(full_path))
    return file_full_path_list


# root_dir = input("Enter root dir: ")

# file_list = traverse_dir_tree(root_dir)

# print(file_list)

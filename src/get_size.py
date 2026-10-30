import os
from traverse_dir_tree import traverse_dir_tree

# returns a dictionary with keys being the file size
# and the value being the list of file paths


def get_size_dictionary(file_list: list) -> dict[int, list[str]]:
    file_size_dict = {}
    for file_full_path in file_list:
        file_size = os.path.getsize(file_full_path)
        if file_size not in file_size_dict:
            file_size_dict[file_size] = []
        file_size_dict[file_size].append(file_full_path)
    return file_size_dict


# root_dir = input("Enter dir: ")

# file_list = traverse_dir_tree(root_dir)

# print(get_size_dictionary(file_list))

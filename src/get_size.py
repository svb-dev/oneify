import os

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


file_list = ['test/test_3.txt', 'test/test_level1/text_2.txt',
             'test/text.txt', 'test/text_4.txt']

print(get_size_dictionary(file_list))

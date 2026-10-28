import os
from get_hash import hash_first_1kb, hash_entire_file
import pprint

# returns a dictionary with keys being the sha256 hash of the
# first 1kb of file(s) and value(s) being the list of file paths


def get_1kb_hash_dictionary(file_list: list) -> dict[int, list[str]]:
    one_kb_hash_dict = {}
    for file_full_path in file_list:
        one_kb_hash = hash_first_1kb(file_full_path)
        if one_kb_hash not in one_kb_hash_dict:
            one_kb_hash_dict[one_kb_hash] = []
        one_kb_hash_dict[one_kb_hash].append(file_full_path)
    return one_kb_hash_dict


def get_entire_file_hash_dictionary(file_list: list) -> dict[int, list[str]]:
    entire_file_hash_dict = {}
    for file_full_path in file_list:
        entire_file_hash = hash_entire_file(file_full_path)
        if entire_file_hash not in entire_file_hash_dict:
            entire_file_hash_dict[entire_file_hash] = []
        entire_file_hash_dict[entire_file_hash].append(file_full_path)
    return entire_file_hash_dict


file_list = ['test/test_3.txt', 'test/test_level1/text_2.txt',
             'test/text.txt', 'test/text_4.txt']

pprint.pprint(get_1kb_hash_dictionary(file_list))

pprint.pprint(get_entire_file_hash_dictionary(file_list))

from get_hash_dict import *
from traverse_dir_tree import traverse_dir_tree
from get_size import get_size_dictionary
import os
import pprint

# returns a list of full paths to duplicate files
# 1. test if any files have the same size, if they do
# 2. test if the hashes of the first 1kb of the files and identical , if they are
# 3. test if the complete hashes of files are identical.
# files that have identical complete hashes are duplicates

# returns a dictionary with keys being the sha256 hash of the
# the entire file(s) and value(s) being the list of files' paths


def file_filter(root_dir: str) -> dict[str, list[str]]:
    # get the list of all files in the dir tree
    all_files_list = traverse_dir_tree(root_dir)
    file_size_dict = get_size_dictionary(all_files_list)
    for size in file_size_dict:
        if len(file_size_dict[size]) > 1:
            same_size_files_list = file_size_dict[size]

        same_1kb_hash_dict = get_1kb_hash_dictionary(same_size_files_list)

        same_hash_dict = {}

        for same_1kb_hash in same_1kb_hash_dict:
            if len(same_1kb_hash_dict[same_1kb_hash]) > 1:
                # i = len(same_1kb_hash_dict[same_1kb_hash]) - 1
                # if os.path.getsize(same_1kb_hash_dict[same_1kb_hash][0]) <= 1024:
                #    same_hash_dict[same_1kb_hash] = same_1kb_hash_dict[same_1kb_hash]
                # else:
                entire_file_hash_dict = get_entire_file_hash_dictionary(
                    same_1kb_hash_dict[same_1kb_hash])
                for entire_hash_key in entire_file_hash_dict:
                    if len(entire_file_hash_dict[entire_hash_key]) > 1:
                        same_hash_dict[entire_hash_key] = entire_file_hash_dict[entire_hash_key]

                # same_hash = get_entire_file_hash_dictionary(
                #    same_1kb_hash_dict[same_1kb_hash])
    # return same_1kb_hash_dict, entire_hash_list
    return entire_file_hash_dict
# OCT 28 : why


root_dir = "test_2"

pprint.pprint(file_filter(root_dir))

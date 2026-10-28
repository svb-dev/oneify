from get_hash_dict import *

# returns a list of duplicate files
# 1. test if any files have the same size, if they do
# 2. test if the hashes of the first 1kb of the files and identical , if they are
# 3. test if the complete hashes of files are identical.
# files that have identical complete hashes are duplicates


def file_filter(root_dir: str) -> list[str]:

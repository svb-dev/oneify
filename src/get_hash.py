import hashlib

# hashes the first 1kb of a file with md5 and returns
# the md5 hash


def hash_first_1kb(file_path: str) -> str:
    hasher = hashlib.md5()
    with open(file_path, "rb") as f:
        # Read up to 1024 bytes
        chunk = f.read(1024)
    hasher.update(chunk)

    return hasher.hexdigest()


print(hash_first_1kb("test/test_3.txt"))

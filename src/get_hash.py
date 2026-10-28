import hashlib

# hashes the first 1kb of a file with SHA-256 and returns
# the hash


def hash_first_1kb(file_path: str) -> str:
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Read up to 1024 bytes
        chunk = f.read(1024)
    hasher.update(chunk)

    return hasher.hexdigest()


# print(hash_first_1kb("test/test_3.txt"))


# hashes the first entire file with SHA-256 and returns
# the hash

def hash_entire_file(file_path: str) -> str:
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Read the entire file
        chunk = f.read()
    hasher.update(chunk)

    return hasher.hexdigest()


# print(hash_entire_file(("test/test_3.txt"))

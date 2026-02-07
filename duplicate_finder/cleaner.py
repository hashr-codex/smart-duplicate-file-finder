import os
from .hasher import get_file_hash

def find_duplicates(folder_path):
    hashes = {}
    for root, _, files in os.walk(folder_path):
        for file in files:
            path = os.path.join(root,file)
            file_hash = get_file_hash(path)
            if file_hash in hashes:
                hashes[file_hash].append(path)
            else:
                hashes[file_hash] = [path]
    return {h: paths for h, paths in hashes.items() if len(paths) > 1}

def interactive_clean(duplicates):
    for hash_value, files in duplicates.items():
        print("\nDuplicates group:")
        for i, file in enumerate(files):
            print(f"{i}: {file}")
            choice = input("Type index to KEEP, or 's' to skip: ")
            if choice.lower() == 's':
                continue

            keep_index = int(choice)

            for i, file in enumerate(files):
                if i != keep_index:
                    os.remove(file)
                    print(f"Deleted: {file}")

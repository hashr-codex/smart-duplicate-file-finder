from duplicate_finder.cleaner import find_duplicates, interactive_clean

folder ="C:/Users/harsh/Downloads"

dups = find_duplicates(folder)

if not dups:
    print("No duplicates found.")
else:
    interactive_clean(dups)
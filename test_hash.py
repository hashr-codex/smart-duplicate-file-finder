from duplicate_finder.hasher import get_file_hash

file1 = "C:/Users/harsh/Downloads/text1.txt"
file2 = "C:/Users/harsh/Downloads/text2.txt"

print(get_file_hash(file1))
print(get_file_hash(file2))
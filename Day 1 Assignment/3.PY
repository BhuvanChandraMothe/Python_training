# Question-3:
# Given a directory, find out the file Name 
# having max size recursively 

import os
from collections import OrderedDict

# def get_file_sizes(directory):
#     file_sizes = {}
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             file_path = os.path.join(root, file)
#             file_name = os.path.basename(file_path)
#             file_size = os.path.getsize(file_path)
#             file_sizes[file_name] = file_size
#     return file_sizes

def get_file_sizes(directory):
    file_sizes = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_name = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)
            file_sizes[file_name] = file_size
    
        sorted_file_size = OrderedDict(sorted(file_sizes.items(), reverse=True))
    return sorted_file_size

# Example usage
directory_path = 'C:/Users/Mothe Bhuvan Chandra/Desktop/Day 1 Assignment'
file_sizes = get_file_sizes(directory_path)
for file_name, size in file_sizes.items():
    print(f"{file_name}: {size} bytes")


    
    

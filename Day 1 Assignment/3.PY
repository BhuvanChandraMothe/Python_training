# Question-3:
# Given a directory, find out the file Name 
# having max size recursively 

import os



# def get_file_sizes(directory):
#     file_sizes = {}
#     for root,dir ,files in os.walk(directory):
#         for file in files:
#             file_path = os.path.join(root, file)
#             file_name = os.path.basename(file_path)
#             file_size = os.path.getsize(file_path)
#             file_sizes[file_name] = file_size
    
#         sorted_file_size = (sorted(file_sizes.items(), reverse=True))
#     print(sorted_file_size)

def get_file_sizes(directory):
    max_size = 0
    largest_file = ""
    for dirpath, dirname, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(dirpath, file)
            file_name = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)
        
            if file_size>max_size:
                max_size = file_size
                largest_file = file_name
    print(f"The largest file is {largest_file} which is {max_size} bytes.")


directory_path = 'C:/Users/Mothe Bhuvan Chandra/Desktop/Day 1 Assignment'
file_sizes = get_file_sizes(directory_path)
# for file_name, size in file_sizes.items():
#     print(f"{file_name}: {size} bytes")



    
    

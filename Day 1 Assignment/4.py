# Question-4:
# Recurively go below a dir and based on filter, dump those files in to  single file 
# (work with only text file)


import os

def read_and_write_files(source_dir, output_file):
    with open(output_file, "w", encoding="utf-8") as out_file:
        for root, _, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as in_file:
                        out_file.write(f"--- Content of {file_path} ---\n")
                        out_file.writelines(in_file.readlines())
                        out_file.write("\n\n")
                except Exception as e:
                    print(f"Could not read {file_path}: {e}")

# Set your directory and output file path
source_directory = "C:/Users/Mothe Bhuvan Chandra/Desktop/Day 1 Assignment"
output_file_path = "c.txt"

read_and_write_files(source_directory, output_file_path)
print(f"All files' contents are written to {output_file_path}")



    
    

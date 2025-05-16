import os
import shutil

# Define the source directory (current directory) and the destination directory
source_dir = os.getcwd()
destination_dir = os.path.join(source_dir, "svg_files")

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Walk through the directory tree
for root, _, files in os.walk(source_dir):
    for file in files:
        if file.endswith(".svg"):
            source_file = os.path.join(root, file)
            destination_file = os.path.join(destination_dir, file)
            
            try:
                # Copy the file to the new folder
                shutil.copy2(source_file, destination_file)
                print(f"Copied: {source_file} -> {destination_file}")
            except shutil.SameFileError:
                print(f"Skipped (SameFileError): {source_file}")

print(f"All SVG files have been copied to {destination_dir}.")

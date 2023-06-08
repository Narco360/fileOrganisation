import os
import shutil

def organize_files(directory):
    # Create subdirectories if they don't exist
    os.makedirs(os.path.join(directory, "Other"), exist_ok=True)

    # Get all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    for file in files:
        # Get the file extension
        _, extension = os.path.splitext(file)

        if extension:
            # Remove the dot from the extension
            extension = extension[1:]

            # Create subdirectory for the extension if it doesn't exist
            os.makedirs(os.path.join(directory, extension), exist_ok=True)

            # Move the file to the respective subdirectory
            src = os.path.join(directory, file)
            dst = os.path.join(directory, extension, file)
            shutil.move(src, dst)
            print(f"Moved file: {file} -> {dst}")
        else:
            # Move files with no extension or unrecognized extension to "Other" subdirectory
            src = os.path.join(directory, file)
            dst = os.path.join(directory, "Other", file)
            shutil.move(src, dst)
            print(f"Moved file: {file} -> {dst}")

    print("\nOrganization complete. Files have been organized into subdirectories.")

# Prompt the user to provide the directory path
directory = input("Enter the directory path to organize: ")

# Call the function to organize files
organize_files(directory)

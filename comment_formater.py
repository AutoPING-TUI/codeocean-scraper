import os
import sys


def replace_comments_in_file(file_path):
    with open(file_path, "r+", encoding="utf-8") as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        for line in lines:
            if line.strip().startswith("//"):
                line = line.replace("//", "#", 1)
            file.write(line)


def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        print(f"Parsing {root}")
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                replace_comments_in_file(file_path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python comment_formater.py <directory_path>")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    process_directory(directory_path)

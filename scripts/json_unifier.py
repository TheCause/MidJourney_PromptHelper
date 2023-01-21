# script for unifying json files

import json
import os
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python json_unifier.py <path_to_json_files>")
        sys.exit(1)

    path = sys.argv[1]
    if not os.path.exists(path):
        print("Path does not exist")
        sys.exit(1)

    if not os.path.isdir(path):
        print("Path is not a directory")
        sys.exit(1)

    files = os.listdir(path)
    if len(files) == 0:
        print("Directory is empty")
        sys.exit(1)

    data = []
    for file in files:
        with open(path + "/" + file) as f:
            data += json.load(f)

    # Create a new variable to store the cleaned data
    cleaned_data = []

    # Loop through the data elements and clean up the prompt keys
    for item in data:
        prompt = item['prompt']
        if prompt is None:
            continue
        # Replacing the '\"' characters with nothing
        prompt = prompt.replace('"', '')
        # Replacing the '\n' characters with nothing
        prompt = prompt.replace('\n', '')
        # Replacing multiple spaces with a single space
        prompt = ' '.join(prompt.split())
        item['prompt'] = prompt
        cleaned_data.append(item)

    # replace the data with the cleaned data
    data = cleaned_data

    with open("unified.json", "w") as f:
        json.dump(data, f)

if __name__ == "__main__":
    main()

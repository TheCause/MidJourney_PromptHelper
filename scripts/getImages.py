import json
import os
import re
import urllib.request

# Create imgs directory if it doesn't already exist
if not os.path.exists('imgs'):
    os.makedirs('imgs')

# Load JSON file using json.load()
with open('unified.json', 'r') as f:
    json_data = json.load(f)

# Initialize existing data
existing_data = []

# Loop through data items and retrieve image links
for item in json_data:
    url = item['url']
    # Create a filename from the other keys of the data item
    filename = ''
    for key, value in item.items():
        if key != 'url':
            filename += value.replace(' ', '_') + '_'
    filename = re.sub(r'[^\w_]', '', filename) + '.png'
    # Create a full filepath to save the image
    filepath = os.path.join('imgs', filename)
    # Check if the file has already been downloaded
    if os.path.exists(filepath):
        print(f'{filename} already exists, skipping...')
        new_item = item.copy()
        new_item['url'] = os.path.relpath(filepath, '.')
        existing_data.append(new_item)
        continue
    try:
        # Download the image using urllib.request.urlretrieve
        urllib.request.urlretrieve(url, filepath)
        print(f'{filename} downloaded successfully')
    except urllib.error.URLError as e:
        print(f'An error occurred while downloading {filename}: {e.reason}')
    except urllib.error.HTTPError as e:
        print(f'An error occurred while downloading {filename}: {e.reason}')
    new_item = item.copy()
    new_item['url'] = os.path.relpath(filepath, '.')
    existing_data.append(new_item)

# Save the updated data to unified_local.json file
with open('unified_local.json', 'w') as f:
    json.dump(existing_data, f)

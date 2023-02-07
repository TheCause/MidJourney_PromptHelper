import firebase_admin
import json
import time
import sys
from firebase_admin import credentials
from firebase_admin import storage

# initialize firebase
my_storage_bucket = 'YOURAPP.appspot.com'
cred = credentials.Certificate("firebaseconf.json")
try:
    firebase_admin.initialize_app(cred, {
        'storageBucket': my_storage_bucket
    })
except Exception as e:
    print("Error initializing firebase:", e)
    sys.exit(1)

bucket = storage.bucket()

# load JSON file
try:
    with open("../unified_local_cleaned.json", "r") as json_file:
        data = json.load(json_file)
except Exception as e:
    print("Error loading JSON file:", e)
    sys.exit(1)

# upload files and replace URLs in the JSON file
for entry in data:
    file_path = entry["url"]
    blob = bucket.blob(file_path)
    try:
        blob.upload_from_filename(file_path)
        blob.make_public()
        entry["url"] = blob.public_url
        print("Uploaded file:", blob.public_url)
    except Exception as e:
        print("Error uploading file:", e)

# save the modified JSON file
timestamp = int(time.time())
try:
    with open("../unified_local_cleaned_firebase_" + str(timestamp) + ".json", "w") as json_file:
        json.dump(data, json_file, indent=2)
except Exception as e:
    print("Error saving modified JSON file:", e)
    sys.exit(1)

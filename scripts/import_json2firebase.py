import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

# Initialize Firebase connection
cred = credentials.Certificate("firebaseconf.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://YOURAPP-default-rtdb.europe-west1.firebasedatabase.app/'
})

# Load JSON data
with open('../unified_local_cleaned_firebase.json', 'r') as file:
    data = json.load(file)

# Add data to Firebase
ref = db.reference('/data')
for item in data:
    ref.push(item)

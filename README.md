data extractions based on "V4 Midjourney Reference Sheets"

/!\ if you have information about the creator of this spreadsheet, please give it to me so that I can inform the users that all the data on which exist thanks to him. 

the idea is to get the data from the google sheet and format them to allow another use (webapp/site etc...)

It is obvious that this procedure does not allow to automate the updates but there are always other ways to do it

## Preamble
Not knowing how to manipulate programmatically google sheets and considering the size of this one, I preferred :

1 - create a new document per tab (manually, about 20 minutes)

2 - export each document in HTML format (manually, about 20 minutes)

3 - use BeautifulSoup to parse the HTML files (script available and html files in the htmls/ directory)

4 - upload the images (script available and files in the imgs/ directory)


## 1 - Create a new document per tab

### A - Copy the Google Sheet to your drive
- Go to the google sheet : https://docs.google.com/spreadsheets/d/1MsX0NYYqhv4ZhZ7-50cXH1gvYE2FKLixLBvAkI40ha0/edit#gid=448521687
- Make a copy of the document : "File" tab then "Make a Copy"
![[screenshots/copy_document.png]]

### B - Extract each tab in a new google sheet

There are 13 differents tabs

- [ ] Characters
- [ ] Landscapes
- [ ] Cartoons, Comics => Cartoons_Comics
- [ ] Paintings
- [ ] Anime, Anthromorph => Anime_Anthromorph
- [ ] Sci-fi
- [ ] Creatures
- [ ] Mediums, Techniques => Mediums_Techniques
- [ ] Time Periods/Fashion => Time_Periods_Fashion
- [ ] Print Media => Print_Media
- [ ] Styles
- [ ] Games
- [ ] Misc

For each of them, 
- Right click on the tab.
- "Copy to" => "New spreadsheet"

![[screenshots/New_spreadsheet.png]]

![[screenshots/Successfully_copied.png]]

- Click on "Open spreadsheet".
- Rename the new spreadsheet
![[screenshots/rename_spreadsheet.png]]

## Export each document in HTML format
> Why not use the .CSV download?
> Because there is no link to the image files :p 

This operation can be done in the previous step.
- Open the new file
- File => Download => Web Page (.html)

The files are in zip format so you just have to unzip them.
> Why make simple when you can make complicated ?

```shell
for i in $(ls -1 | sed -e 's/\.zip$//'); do unzip $i.zip -d $i && rm $i.zip; done
```

## 3 - use BeautifulSoup to parse the HTML files (script available and html files in the htmls/ directory)

All python scripts for extracting json from html are in ./scripts repository.

I could merge all the scripts into one, but I won't do that for now :p 

/!\ the results are in the .jsons directory


## 4 - upload the images (script available and files in the imgs/ directory)

use the python script: getimages.py which uploads the images to the imgs directory and creates a unified_local.json file which contains the local urls

The images are not kept in the repository because there are 3031 images for 367M

## 5 - json cleaning

comment j'ai fait pour nettoyer le fichier json

## 6 - setting firebase - Optional if you want to used data in web project

Firebase is a real-time back-end development service developed by Google. It offers a variety of features such as database management, authentication, file storage and more. In this tutorial, we will show you how to create a new Firebase.

#### Prerequisites

- An active Google account

#### Access the Firebase console

- Access the Firebase console by logging in with your Google account at [https://console.firebase.google.com/](https://console.firebase.google.com/)

#### Create a new database

- Click on the "Create a Firebase" button
- Enter a name for your Firebase
- Select an existing project or create a new project
- Click on the "Create a database" button

#### Configure authentication

- In the "Authentication" section, click on the "Configure authentication" button
- Select the desired authentication methods : Google
- Configure the settings for each selected authentication method
- Click the "Save" button to save changes

#### Edit Firebase security rules

- Modify Firebase security rules to allow reading and writing for authenticated users

```yaml
service firebase.storage {
  match /b/{bucket}/o {
    match /{allPaths=**} {
      allow read: if request.auth != null || !request.auth;
      allow write, update, delete: if request.auth != null;
    }
  }
}
```

#### upload & change url

- create firebaseconf.json file with data given https://console.firebase.google.com/project/yourprojectID/settings/serviceaccounts/adminsdk

```json
{
    "type": "service_account",
    "project_id": "Your_Project",
    "private_key_id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "private_key": "-----BEGIN PRIVATE KEY-----xxxxxxxxxxxxxxxx-----END PRIVATE KEY-----\n",
    "client_email": "",
    "client_id": "",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/xxxxx"
  }
```

- execute : upload2firebase.py for uploading imgs in Firebase Bucket and change URL values in .json file
- execute : import_json2firebase.py for integrate new json file on Firebase Db

## Sources

[V4 Midjourney Reference Sheets](https://docs.google.com/spreadsheets/d/1MsX0NYYqhv4ZhZ7-50cXH1gvYE2FKLixLBvAkI40ha0/edit#gid=448521687) 

## Another prompt helper

https://ckovalev.com/midjourney-ai/styles
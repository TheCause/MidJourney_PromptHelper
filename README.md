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

The images are not kept in the repository because there are 2946 images for 359M

## Sources

[V4 Midjourney Reference Sheets](https://docs.google.com/spreadsheets/d/1MsX0NYYqhv4ZhZ7-50cXH1gvYE2FKLixLBvAkI40ha0/edit#gid=448521687) 

## Another prompt helper

https://ckovalev.com/midjourney-ai/styles
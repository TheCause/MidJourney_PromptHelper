from bs4 import BeautifulSoup
import pandas as pd
import json

# Open the html file
filename = "../htmls/Paintings/Paintings.html"

with open(filename, encoding='utf-8') as f:
    soup = BeautifulSoup(f, "html.parser")

# Find the table with class "waffle"
table = soup.find("table", class_="waffle")
rows = table.find_all("tr")

# Extract data from the table
data = []
for row in rows:
    cells = row.find_all("td")
    values = []
    for cell in cells:
        if cell.text.strip() != "":
            values.append(cell.text)
        if cell.find("img"):
            img = cell.find("img")
            src = img["src"]
            values.append(src)
    data.append(values)

# Create a pandas dataframe from the extracted data
df = pd.DataFrame(data)

# Remove all rows with missing data
df.dropna(axis=0, how="all", inplace=True)

# Remove lines without interest
df = df.drop(df.index[0])

# switch col0 et col1
df.iloc[:, [0, 1]] = df.iloc[:, [1, 0]].values

# new index
df = df.reset_index(drop=True)

# Header setting
df.rename(columns=df.iloc[0], inplace=True)
df = df.iloc[1:]

data = []
for i, row in df.iterrows():
    artist = row[df.columns[0]]
    date_range = row[df.columns[5]]
    location = row[df.columns[6]]
    categrory = "Paintings"
    for j in range(1, len(df.columns)):
        prompt = df.columns[j]
        url = row[j]
        if "https" in url:
            data.append({'artist': artist, 'prompt': prompt, 'url': url, 'date_range':date_range, 'location': location, 'category': categrory })

json_data = json.dumps(data)

# Save the json data to a file
with open("../jsons/Paintings.json", "w") as f:
    json.dump(json.loads(json_data), f)
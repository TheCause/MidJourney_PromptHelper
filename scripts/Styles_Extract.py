from bs4 import BeautifulSoup
import pandas as pd
import json

# Open the html file
filename = "../htmls/Styles/Styles.html"
#headers = ["Era", "URL1", "URL2", "URL3", "URL4"]
with open(filename) as f:
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
df = df.drop(df.index[[0,3]])

# Transpose the dataframe
df_transposed = df.transpose().copy()

# Set the first row as the column headers
df_transposed.columns = df_transposed.iloc[0]
# Create a list to store the json data
result = []

# Store the first column as "prompt"

prompt = df_transposed.iloc[:, 0].tolist()
# Iterate over the columns

for i in range(1, len(df_transposed.columns)):
    style = df_transposed.columns[i]

    # Iterate over the rows
    for j in range(len(df_transposed)):
        data = {}
        data["style"] = style
        data["prompt"] = prompt[j]
        data["url"] = df_transposed.iloc[j, i]
        data["category"] = "Styles"
        if "https" in data["url"]:
            result.append(data)

# Convert the list to json
json_data = json.dumps(result)

# Save the json data to a file
with open("../jsons/Styles.json", "w") as f:
    json.dump(json.loads(json_data), f)
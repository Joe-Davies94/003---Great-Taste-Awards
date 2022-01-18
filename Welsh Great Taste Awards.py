# Identify and report the number of Welsh Great Taste Awards

from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import date

# Set variable to current date
today=date.today()
today=today.strftime("%Y-%m-%d")

# Create empty dataframe
df=pd.DataFrame({
})

# Input for either 2020 or 2021. 2019 and before doesn't work due to different url structure
print("Enter year 2020 or 2021: ")
year = input()
if year == str(2020):
    years=2020
else:
    year=""
    years=2021
print(years)


# Function for identifying ratings
def countFunction(county_id, name):
    global df
    global year

    # gets the html of each Welsh county
    url = requests.get(
        "https://greattasteawards.co.uk/results"+str(year)+"?_token=8c3gzxgcKmBFflUOBlAITyxSMrHPeVhdRdcofLli&sort_options_limit=50&sort_options_sort_direction=desc&sort_options_sort_by=rating&Keyword=&mg_rating_id=&mg_category_id=&country_id=&county_id="+str(county_id)+"&filter=Search"
        )
    bsurl = BeautifulSoup(url.text, "html.parser")
    
    # Counts the number of awards in total and at each rating per county
    products = len(bsurl.find_all('td', attrs={'data-title': 'Product name'}))
    ratings3 = len(bsurl.find_all('img', attrs={'src': '/images/three_star.png'}))
    ratings2 = len(bsurl.find_all('img', attrs={'src': '/images/two_star.png'}))
    ratings1 = len(bsurl.find_all('img', attrs={'src': '/images/star.png'}))

    # Adds the counts to a data frame df2, and append df2 to the main data frame df    
    df2 = pd.DataFrame({
    "All Awards":[products],
    "3-Star Awards":[ratings3],
    "2-Star Awards":[ratings2],
    "1-Star Awards":[ratings1],
    })
    df2.index = [str(name)]

    df = df.append(df2)
    return df

# Run the above function for each Welsh county
countFunction("116", "Carmarthenshire")
countFunction("117", "Ceredigon")
countFunction("118", "Clwyd")
countFunction("119", "Denbighshire")
countFunction("120", "Flintshire")
countFunction("121", "Glamorgan")
countFunction("122", "Gwent")
countFunction("123", "Gwynedd")
countFunction("124", "Anglesey")
countFunction("125", "Mid-Glamorgan")
countFunction("126", "Monmouthshire")
countFunction("127", "Pembrokeshire")
countFunction("128", "Powys")
countFunction("129", "Rhondda")
countFunction("130", "South Glamorgan")
countFunction("131", "West Glamorgan")

# Add total row to data frame and export to excel
df.loc["Total"] = df.sum()
df.to_excel(today+" - Great Taste Awards "+str(years)+".xlsx")

print("Complete")


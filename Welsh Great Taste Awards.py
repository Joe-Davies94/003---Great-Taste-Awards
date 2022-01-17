from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import date

df=pd.DataFrame({
})

""" Commented out - not working yet

print("Enter year 2020 or 2021: ")
year = input()
if year == 2020:
    year=2020
    years=2020
else:
    year=""
    years=2021

"""


def countFunction(county_id):
    global df

    # gets the html of each Welsh county
    url = requests.get(
        "https://greattasteawards.co.uk/results?_token=8c3gzxgcKmBFflUOBlAITyxSMrHPeVhdRdcofLli&sort_options_limit=50&sort_options_sort_direction=desc&sort_options_sort_by=rating&Keyword=&mg_rating_id=&mg_category_id=&country_id=&county_id="+str(county_id)+"&filter=Search"
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
    df2.index = [str(county_id)]

    df = df.append(df2)
    return df

# Run the above function for each Welsh county
countFunction("116")
countFunction("117")
countFunction("118")
countFunction("119")
countFunction("120")
countFunction("121")
countFunction("122")
countFunction("123")
countFunction("124")
countFunction("125")
countFunction("126")
countFunction("127")
countFunction("128")
countFunction("129")
countFunction("130")
countFunction("131")

df.loc["Total"] = df.sum()

df.to_excel("Great Taste Awards.xlsx")

print("Complete")


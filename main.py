from bs4 import BeautifulSoup
import requests

# GET YEAR
year = input("Year of Interest?: ")

# Initialize List of Categories
categories = []

url = f"https://www.pro-football-reference.com/years/{year}/leaders.htm"
response = requests.get(url).content

# Create Soup
soup = BeautifulSoup(response, "html.parser")

# Find the categories
leaders = soup.find("div", {"class": "data_grid"}).findChildren("caption")
for i in leaders:
    categories.append(i.text)
    print(i.text)

# Prompt User for category of interest
category = input("Which category would you like to see?")

# Using user inputted category, find list of leaders and stats
if category in categories:
    x = soup.find_all("caption")
    for i in x:
        if i.text == category:
            table = i.findParent('table')
            leaderboard = table.findChildren("td", {"class": "who"})
            for leader in leaderboard:
                print(
                    f"{leader.find('a').text} - {leader.findParent('table').findChild('td', {'class': 'value'}).text}")

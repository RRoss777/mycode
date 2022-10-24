#!/usr/bin/env python3

"""Alta3 Research | RRoss | ryanne.ross@tlgcohort.com |
- Eat Seasonally with Python Recipe Generator"""

"""Description:
A script to interact with an "open" api,
https://tasty.p.rapidapi.com/recipes/auto-complete
documentation for the API is available via,
https://rapidapi.com/apidojo/api/tasty"""

#import necessary module
import requests

#base API location
url ="https://tasty.p.rapidapi.com/recipes/auto-complete"

#dictionary of seasons and corresponding produce available during that season
#seasonal_ingredients = [{"season": "Spring", "seasonal_produce": [ "apples”, “carrots”, “fennel”]}, {"season": "Summer", "seasonal_produce": ["apples", "blueberries", "melons"]},  {"season": "Fall", "seasonal_produce": ["apples", "beets", "pumpkin"]}, [{"season": "Winter", "seasonal_ produce": ["apples", "beets", "sweet potatoes”]}]
seasonal_ingredients = [{"Spring": ["apples”, “carrots”, “fennel"]}, {"Summer": ["apples", "blueberries", "melons"]}, {"Fall": ["apples", "beets", "pumpkin"]}, {"Winter": ["apples", "beets", "sweet potatoes”]}]

    a = seasonal_ingredients.keys[0][0]
    b = seasonal_ingredients.keys[1][0]
    c = seasonal_ingredients.keys[2][0]
    d = seasonal_ingredients.keys[3][0]

x = print(input(“Eating produce when it is in season not only tastes better but is also nutritionally better for you. Which season are you interested in for trying out new recipes? Enter {a}, {b} {c} or {d} to find out what produce is in season.”))

def produce_list():

if a in seasonal_ingredients:
print(list(a))
elif b in seasonal_ ingredients:
print(list(b))
elif c in season_ingredients:
print(list(c))
elif d in seasonal_ingredients:
print(list(d))
else 
x =print (input(f“Incorrect entry. Please enter {a}, {b}, {c} or {d} to review a list of seasonal produce”)

produce_list()

#x represents search term (an item listed within seasonal produce)
seasonal_produce = {"prefix":"x"}
headers = {
	"X-RapidAPI-Key": "c128904005msh4fead8e6880b787p190c28jsnc61fb0472938",
	"X-RapidAPI-Host": "tasty.p.rapidapi.com"
}
response = requests.request(“GET”, url, headers=headers, params=seasonal_produce)
print(response.text)

counter = 0
with open("response.text", "r") as recipe1:
print(recipe1.read())
counter += 1
print(f"There are {counter} recipes containing {x} listed above")


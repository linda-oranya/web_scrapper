from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import numpy as np
import time
import random
import json

headers = ({'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit\
# /537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})

page_number = 1
base_url = f"https://www.cheki.co.ke/vehicles?page={page_number}"
response = get(base_url, headers=headers)
html_soup = BeautifulSoup(response.text, 'html.parser')
content_list = html_soup.find_all(
    'div', attrs={'class': 'right-card-part-container'})

categories = {
    "Transmission": ["Automatic", "Manual"],
    "Condition": ["Foreign Used", 'Locally Used', 'Used', 'Brand New'],
    "Fuel-Type": ["Petrol", "Diesel", 'Hybrid & Electrical'],
    "Color": ["White", "Silver", "Blue", "Yellow", "Red", "Black", "Brown", "Gold", "Orange", "Pink", "Purple", "Pearl", "Dark Blue" "Other"]
}


cat_keys = categories.keys()

car_data = []
for i in content_list:
    car_info = i.find_all('li', class_='ellipses')
    car_details = {}
    for i in range(0, len(car_info)):
        j = car_info[i]
        car_property = j.text.strip()

        # things we are trying to hack
        if i == 0:
            car_details["Country"] = car_property
        if "km" in car_property:
            car_details["Mileage"] = car_property
        if len(car_property) == 4:
            car_details["Year"] = car_property

        # things in dictionary, that are have recognizable pattern
        for category in cat_keys:
            if categories[category].count(car_property) > 0:
                car_details[category] = car_property
                break

    car_data.append(car_details)

print(car_data)


# df = pd.DataFrame(info,columns=['Location','Transmission','Color','How_used','Year','Fuel_Type'])
# print(df)
# print(infos)

#dict1 = list(info)
# dict2 = info[1]
# dict3 = info[2]
# dict4 = info[3]
# dict5 = info[4]
# dict6 = info[5]
# dict7 = info[6]
# print(dict1)
# df = pd.DataFrame(data=[dict1,dict2,dict3,dict4,dict5,dict6,dict7],columns=['Location','Transmission','Color','How_used','Year','Fuel_Type'])
# print(df)


# df = pd.DataFrame(np.array(info).reshape(-1,7), columns =['Location','Transmission','Color','Mileage','Use', 'Year', 'Fuel_type'])
# print (df)

# for i in .text.strip():
#     print(i)

# # def get_basic_info(content_list):
# #     basic_info = []
# #     for item in content_list:
# #         basic_info.append(item.find_all('span', attrs={'class': 'ellipses'}))
# #     return basic_info
#
# def get_car_details(car_details):
#     car_info = []
#     for ul in car_details:
#            car_info.append(ul.find_all('li', attrs={'class': 'ellipses'}))
#     return car_info
#
#
# def get_price_details(price_details):
#     price_info = []
#     for item in price_details:
#            price_info.append(item.find_all('div',attrs={'class': 'right-side-desktop-card'}))
#     return price_info
#
#
# def get_names(basic_info):
#     names = []
#     for item in basic_info:
#         for i in item:
#             names.append(i.find_all("span", attrs={"class": "ellipses"})[0].text.strip())
#
#     return names
#
# def get_towns(car_info):
#     towns = []
#     for item in car_info:
#         for i in item:
#             towns.append(i.find_all("li", attrs={"class": "ellipses location-container"}))
#     return towns
# page_number=1
# base_url = "https://www.cheki.co.ke/vehicles?page={}".format(page_number)
# response = get(base_url, headers=headers)
# html_soup = BeautifulSoup(response.text, 'html.parser')
# content_list = html_soup.find_all('div', attrs={'class': 'right-card-part-container'})
# car_info = get_car_details(content_list)
# #print(car_info)
#
#
# def get_transmission(car_info):
#     transmissions = []
#     for item in car_info:
#         transmissions.append(item[1].text.strip())
#     return transmissions
#
#
# def get_colors(car_info):
#     colors = []
#     for item in car_info:
#             colors.append(item[2].text.strip())
#     return colors
#
# def get_mileages(car_info):
#     mileages = []
#     mileage = []
#     for item in car_info:
#             mileages.append(item[3].text.strip())
#             # for j in mileages:
#             #     if j not in ('Foreign Used', 'Locally Used', 'Brand New'):
#             #         mileage.append(j)
#     return mileages
#
#
# def get_use(car_info):
#     how_used = []
#     grade_use = []
#     for item in car_info:
#             how_used.append(item[4].text.strip())
#         # for j in how_used:
#         #     if j in ('Foreign Used','Locally Used','Brand New'):
#         #         grade_use.append(j)
#
#     return how_used
#
# def get_years(car_info):
#     years = []
#     for item in car_info:
#         #for i in item:
#        years.append(item[-1].text.strip())
#     return years
#
# #
# def get_negotiables(price_info):
#     negotiables = []
#     for item in price_info:
#         for i in item:
#             negotiables.append(i.find_all("h4", attrs={"class": "label"}))
#     return negotiables
#
# def get_prices(price_info):
#     prices = []
#     for item in price_info:
#         for i in item:
#             prices.append(i.find_all("h2", attrs={"class": "listing-price"})[0].string.replace(u'\xa0', u' ').strip())
#     return prices
#
#
# page_number = 1
# names = []
# towns = []
# transmissions = []
# colors = []
# mileages = []
# how_used = []
# years = []
# negotiables = []
# prices = []
#
# for i in range(9):
#     base_url = "https://www.cheki.co.ke/vehicles?page={}".format(page_number)
#     response = get(base_url, headers=headers)
#     html_soup = BeautifulSoup(response.text, 'html.parser')
#     content_list = html_soup.find_all('div', attrs={'class': 'right-card-part-container'})
#
#     #basic_info = get_basic_info(content_list)
#     car_info = get_car_details(content_list)
#     price_info = get_price_details(content_list)
#
#     #names1 = get_names(basic_info)
#     towns1 = get_towns(car_info)
#     transmissions1 = get_transmission(car_info)
#     colors1 = get_colors(car_info)
#     mileages1 = get_mileages(car_info)
#     how_used1 = get_use(car_info)
#     years1 = get_years(car_info)
#     negotiables1 = get_negotiables(price_info)
#     prices1 = get_prices(price_info)
#
#     #names.extend(names1)
#     towns.extend(towns1)
#     transmissions.extend(transmissions1)
#     colors.extend(colors1)
#     mileages.extend(mileages1)
#     how_used.extend(how_used1)
#     years.extend(years1)
#     negotiables.extend(negotiables1)
#     prices.extend(prices1)
#     page_number = page_number + 1
#     time.sleep(random.randint(1, 2))
#
# cols = ["Town", "Transmission", "Colors", "Mileage (Km)", "How_used", "Years", "Negotiables", "Price"]
# data = pd.DataFrame({ "Town": towns, "Transmission": transmissions, "Colors": colors, "Mileage (Km)": mileages, "How_used": how_used, "Years": years,  "Negotiables": negotiables,  "Price": prices})[
#         cols]
# data["Price"] = data["Price"].replace({'\KSh': ''}, regex=True)
# data["Price"] = data["Price"].replace({'\,': ''}, regex=True)
# data["Mileage (Km)"] = data["Mileage (Km)"].replace({'\ Km': ''}, regex=True)
# data[["Mileage (Km)", "Years", "Price"]] = data[["Mileage (Km)", "Years", "Price"]].apply(
#         pd.to_numeric)
# #data = data.transpose()
# print(data['Name'].head())

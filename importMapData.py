# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 11:16:42 2025

@author: chris
"""

import json
import matplotlib.pyplot as plt
import pandas as pd
import requests
import numpy as np
import stations
output_to_png = True


# Testing out the board using real data

# my first piece of data is the tube map in a JSON file

# Step 1

# The files can be pulled from OpenStreetMaps (implemented)
# Individual file parsing:
#   Need Lat/Lon
#   OPTIONAL: Station Name for future use
#   

# Step 1.5:
# OPTIONAL: in the case of london, there are too many stations to fit on the grid,
#   implement a clustering algorithm to find some square shape in the lat/lon.
#   This strategy may be used when there is one or more of:
#       A: Too many stations 
#       B: Uneven distribution of stations

# Step 2
# Normalize the lat/lon data to the limits of the grid

# Step 3
# Round the new lat/lons to the grid lines
#   Remove overlapping stations. (ties into step 1.5)
#   If there are still overlapping stations, apply a light random filter, 
#       more intense on the edges of the grid

# Step 4
# Distribute starting stations, tourist attractions, and station types (shape).

# River Data:
# Will need to be pulled from open street map. More thought needed.



# ALT: Take raw coordinates of stations in the city. Implement clustering 
#       algorithm that identifies areas with a good enough spread.

def to_png(stationList, city):
    print(f"Outputting transformed station map to {cityDict[usrInp]}.png")
    plt.figure(figsize=(16, 12), dpi=80)
    plt.scatter(stationList[:,1], stationList[:,0])
    plt.savefig(f"{city}.png")


# Individual file parsing:

overpass_url = "http://overpass-api.de/api/interpreter"

loc = "Greater London"

cityDict = {"1": "Greater London", "2": "New York City", "3": "Toronto", "4": "Wien"}
usrInp = ""
print("Enter a number to choose a city:")
print(cityDict)

while (usrInp not in cityDict.keys()):
    usrInp = input()
    
loc = cityDict[usrInp]

query = f"""
[out:json][timeout:25];
area["name"="{loc}"]->.searchArea;
(
  node["railway"="station"]["station"="subway"](area.searchArea);
  way["railway"="station"]["station"="subway"](area.searchArea);
  relation["railway"="station"]["station"="subway"](area.searchArea);
);
out body;
>;
out skel qt;
"""



response = requests.get(overpass_url, params={'data': query})
geojson_data = response.json()
# [[]]
# Save as a GeoJSON file
with open('data.geojson', 'w') as f:
    json.dump(geojson_data, f)
    

# Load GeoJSON file
with open('data.geojson', 'r') as f:
    geo_data = json.load(f)

# Define the bounding box for your area (min_lat, min_lon, max_lat, max_lon)
bounding_box = {
    "min_lat": 40.0,
    "max_lat": 41.0,
    "min_lon": -74.0,
    "max_lon": -73.0,
}

# Function to check if a point is within the bounding box
def is_within_bounding_box(lat, lon, bbox):
    return bbox["min_lat"] <= lat <= bbox["max_lat"] and bbox["min_lon"] <= lon <= bbox["max_lon"]

# Extract metro stations within the bounding box
metro_stations = []

# print(geo_data)
# print(geo_data.keys())
# print(geo_data["elements"][0])
# print(len(geo_data["elements"]))

stationList = np.ndarray((len(geo_data["elements"]),2))
# print(stations)


for ii in range(len(geo_data["elements"])):
    stationList[ii][0] = geo_data["elements"][ii]["lat"]
    stationList[ii][1] = geo_data["elements"][ii]["lon"]

# kdsj
def NormalizeData(data):
    return 2*(data - np.min(data)) / (np.max(data) - np.min(data)) - 1

stationList[:,1] = NormalizeData(stationList[:,1])
stationList[:,0] = NormalizeData(stationList[:,0])


# stations[:,1] = np.sin(stations[:,1]*np.pi/2)
# stations[:,0] = np.sin(stations[:,0]*np.pi/2)
def apply_sin_func(data):
    return np.sin(data*np.pi/2)



stationList[:,1] = apply_sin_func(stationList[:,1])
stationList[:,0] = apply_sin_func(stationList[:,0])

# Takes a set of points, rounds them to the grid (10x10)
# unsure if I want this function (and previous) to be applied to a 2D Array, or just a 1D Array
# This will need to use the Station object
def snap_points_to_grid(data):
    # This function will take 2D Array: "data", of coordinates, and round 
    #   them to a 10x10 grid (custom grid sizes to come?)
    # Requires: NormalizeData() function
    
    # Normalize, then multiply by 9, then round to integer
    data[:,1] = NormalizeData(data[:,1])
    data[:,0] = NormalizeData(data[:,0])
    
    data = data * 9
    
    data = data.round()
    return data
    pass

stationList = snap_points_to_grid(stationList)
# df = pd.DataFrame(geo_data["elements"])
# df = df.filter(["lat", "lon"])


# print(df[13])

# plt.figure(1)
# plt.scatter(df["lon"], df["lat"])
# plt.savefig(f"{cityDict[usrInp]}.png")



if output_to_png:
    to_png(stationList, cityDict[usrInp])
    # print(f"Outputting transformed station map to {cityDict[usrInp]}.png")
    # plt.figure(figsize=(16, 12), dpi=80)
    # plt.scatter(stations[:,1], stations[:,0])
    # plt.savefig(f"{cityDict[usrInp]}.png")




# for feature in geo_data["elements"]:
#     properties = feature["properties"]
#     geometry = feature["geometry"]
    
#     if properties.get("station") == "subway" or properties.get("railway") == "station":
#         lat, lon = geometry["coordinates"][1], geometry["coordinates"][0]
#         if is_within_bounding_box(lat, lon, bounding_box):
#             metro_stations.append(properties["name"])

# print("Metro stations in the area:", metro_stations)


# Matthew Williams Weather Forecast Project 30/01/2025.
# weather_file_IO_module.py.

import json
import string
import time
import re
import weather_module

path = r"C:\Users\44780\OneDrive\Documents\Just-IT Project\Python\Python_Projects\Weather_Forecast"
weather_file_name = "weather_data.json"
weather_data_file = f"{path}\{weather_file_name}"
cities_file_name = "world_cities.txt"
cities_data_file = f"{path}\{cities_file_name}"

# Copy weather_data.json file into weather_data dictionary.
def loadJson():
    weather_data={}
    try:
        if not weather_data:
            with open(weather_data_file, "r", encoding="utf-8") as file:
                weather_data = json.load(file) 
                file.close()                   
                print("The weather_data.json file has been successfully loaded")                
    except Exception as e:
        print(f"An error loading data occurred: {e}")    
    return weather_data

# Write new data to weather_data.json file.
def writeFile(weather_data):    
    weather_data=alphaSortDict(weather_data)
    try:
        with open(weather_data_file, "w") as file:
            json.dump(weather_data, file, indent=4)
            file.close()
            time.sleep(1)
            print("\nUpdate successful")
            weather_module.startUp(weather_data)            
    except Exception as e:
        print(f"File write exception error occurred: {e}")        
        weather_module.startUp(weather_data) 

# Delete data from weather_data dictionary and send to writeFile() for 
# writing to weather_data.json.
def deleteEntry(weather_data):
    city = string.capwords(input("\nPlease enter the name of a city to be deleted:\n>"))
    if city not in weather_data.keys():
        print(f"Invalid input or city not found: {city}")
        time.sleep(1)
        weather_module.startUp(weather_data) 
    else:
        weather_data.pop(city)
        writeFile(weather_data)

# Sorts weather_data the dictionary into alphabetical order for writing to the weather_data.json file.         
def alphaSortDict(weather_data):
    weather_data = dict(sorted(weather_data.items()))    
    return weather_data   

# Searches a file with 50000 city names.
def checkCityFile(city):
    with open(cities_data_file, 'r', encoding="utf-8-sig") as city_file:
        content = city_file.read()
        city_file.close()
        if re.search(city, content):
            print(f"{city} does exist.")
            return True
        else:
            print(f"{city} doesn't exist.") 
            return False          
        
# EOF
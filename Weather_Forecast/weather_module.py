# Matthew Williams Weather Forecast Project 30/01/2025.
# weather_module.py.

import sys
import string
import time
import weather_file_IO_module

# Start up menu to select which function to use.
def startUp(weather_data):                 
    choice = input("\nPlease choose one of the following options:\n1: To view the weather forecast of a single city, type (1):\n2: To see the weather in all cities, \
type (2):\n3: To add a new city and weather data, type (3):\n4: To delete a city, type (4):\n5: To exit the app, type (5):\n>")    
    try:
        match(choice):
            case "1":
                time.sleep(1)
                getCity(weather_data)
            case "2":
                time.sleep(1)
                displayWeatherAll(weather_data)
            case "3":
                time.sleep(1)
                addWeatherData(weather_data)
            case "4":
                time.sleep(1)
                weather_file_IO_module.deleteEntry(weather_data)                  
            case "5":
                print("\nThank you for using my Python Weather Forecast Application!\n")
                time.sleep(1)
                sys.exit(0)   
            case _:
                print(f'Invalid Input: {choice}')
                startUp()
    except Exception as e:
        print(f"An exception occurred {e}")
        sys.exit(1)        

# Get the chosen city from user and format the city list.
def getCity(weather_data):           
    print('Please enter a city from the below list:')
    cityList = [*weather_data.keys()]    
    cityList = print(", ".join(map(str, cityList)))       
    city = input()
    city = string.capwords(city)
    checkCity(city, weather_data)        
    
# Check the city exists. If not => startMenu().
def checkCity(city, weather_data):
    if city not in weather_data.keys():
        time.sleep(1)
        print(f'\n{city} is not recognised by the weather app, returning to start menu')
        time.sleep(1)
        startUp(weather_data)
    else:
        displayWeather(city, weather_data)                  

# After checking the city exists, display the city and forecast.        
def displayWeather(city, weather_data):
    forecast = weather_data.get(city, weather_data)
    print(f'\nThe weather in {city} is:')
    time.sleep(1)
    try:
        for key, value in forecast.items():
            print(f"{string.capwords(key)}: {value}")              
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    startUp(weather_data)   

# Display all the cities and forecasts.
def displayWeatherAll(weather_data):  
    print(f'\nThe weather in all cities:')
    time.sleep(1)  
    try:
        for key, value in weather_data.items():                        
            print(f"\n{key}:")
            for sub_key, sub_value in value.items():
                print(f"{sub_key}: {sub_value}")
                time.sleep(0.25)
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    startUp(weather_data)
    
# Add a new city. Validates data input.
def addWeatherData(weather_data):   
    try:        
        newCity = string.capwords(input("Enter your new city name:\n>"))
        newCity = checkStrInput(newCity) 
        if newCity not in weather_data and weather_file_IO_module.checkCityFile(newCity):                                
            temp = input("Enter a number for the temperature in celsius:\n>")
            temp = checkNumInput(temp)        
            conditions = string.capwords(input("Enter the conditions such as; Cloudy, Warm or Rainy:\n>"))
            conditions = checkStrInput(conditions)
            wind_speed = input("Enter the wind speed in KM/H:\n>")
            wind_speed = checkNumInput(wind_speed)
            humidity = input("Enter a number for the humidity in %:\n>")
            humidity = checkNumInput(humidity)
            weather_data[newCity] = {"temperature" : temp + "°C", "conditions" : conditions, "wind_speed" : wind_speed + " km/h", "humidity" : humidity + "%"}            
            weather_file_IO_module.writeFile(weather_data)               
        else:
            time.sleep(1)
            print(f"{newCity}: is either already in the database or not a valid city, returning to the start menu.")         
            time.sleep(1)
    except Exception as e:           
        print(f"An error occurred whilst trying to update the weather data: {e}")
        return
    startUp(weather_data)

# Validate the string input from addWeatherData().
def checkStrInput(strInput):
    while True: 
        if not strInput.isalpha() or len(strInput) > 20:            
            time.sleep(1)       
            strInput = input(f"Invalid input: {strInput} - input must be alphabetical and less than twenty characters. Please enter valid input:\n") 
        else:                          
            return strInput
        
# Validate the numerical input from addWeatherData().
def checkNumInput(numInput):
    while True:
        if not numInput.isdigit() or len(numInput) > 2:            
            time.sleep(1)            
            numInput = input(f"Invalid input: {numInput} - input should be a two digit number. Please enter a valid number:")                 
        else:
            return numInput      
        
#  EOF
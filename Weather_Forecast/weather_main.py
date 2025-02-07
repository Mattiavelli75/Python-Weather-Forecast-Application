# Matthew Williams Weather Forecast Project 30/01/2025.
# weather_main.py.

import weather_module
import weather_file_IO_module

# Copies data from .json file into weather_forecast dictionary. 
weather_data = weather_file_IO_module.loadJson()

# Print welcome message. 
print("\nWelcome to my Python Weather Forecast Application")

# Calls the .json import function and executes startUp(). Passes the json file to the startUp() function.
weather_module.startUp(weather_data)

#  EOF
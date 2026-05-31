from datetime import datetime

# This application displays a spreadsheet automation menu
# and converts temperature data from Fahrenheit to Celsius.

print("corger5719 Spreadsheet Automation Menu")
print("1. Input Data")
print("2. View Current Data")
print("3. Generate Report\n")


# The next line retrieves the inputted option and stores into the variable choice.
choice = input("Enter your menu option: \n")


#Mathematical Conversion Function
def convertData(fahrenheit):
    celsius = f"{(fahrenheit - 32) * 5 / 9:.0f}"
    return celsius


#Data Gathering & Iteration Function
def getInput():
    entries = int(input("How many entries are being entered? \n"))

    for entry in range(entries):
        date = input("Enter the date: \n")
        temperature = float(input("Enter the highest temperature for the inputted date in Fahrenheit: \n"))
        
        
        
        # Function Name: convertData
        # Argument Required: temperature (float)
        # Expected Return Value: converted temperature in Celsius (float)
        convertedValue = convertData(temperature)
        

        # Calling convertData function; requires a numerical Fahrenheit value and returns Celsius.
        convertedValue = convertData(temperature)
        

        print("The following was saved at", datetime.now(), ":\n")
        print("Date:", date)
        print("Temperature in Fahrenheit:", temperature)
        print("Temperature in Celsius:\n", convertedValue)
        

#Conditional Logic
if choice == "1":
    getInput()
else:
    print("Error: The chosen functionality is not implemented yet")

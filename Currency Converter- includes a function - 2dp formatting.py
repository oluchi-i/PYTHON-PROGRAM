# Purpose: THIS PROGRAM CONVERTS DOLLARS IN AN ACCOUNT TO EUROS.
# Author:  OLUCHI IKWUEGBU
# Date:    10/08/23

# define the function below this line
def currencyConverter(dollars, rate):
    deductfee = dollars - 10
    conversion = deductfee * rate
    return conversion

# the main script
if __name__ == "__main__":
    # main script code goes below this line. Keep the same indentation level as this line.
    rate = float(input("Enter the Dollar to Euro exchange rate: "))
    dollars = float(input("Enter the amount of Dollars to exchange: "))
    convert = currencyConverter(dollars, rate)
    print("At the current exchange rate of",rate, "you will get", (f'{convert:.2f}'), "Euros")
#Adam Lunn(AMLKM4)------Unit Tests in Python-------Infotc 4320
#Import unittest and datetime
import unittest
from datetime import datetime
import re
#HERE IS THE USER INPUT CLASS THAT WAS GIVEN IN CLASS
class UserInput:
    def get_symbol(self):
        while True:
            symbol = input("Enter the stock symbol you are looking for: ")
            if not self.isValidString(symbol):
                print("ERROR: please enter a stock symbol!\n")
            else:
                return symbol

    def get_chart_type(self):
        valid_selections = ["1", "2"]
        while True:
            self.printChartMenu()
            chart_type = input("Enter the chart type you want (1, 2): ")
            if not self.isValidString(chart_type) or chart_type not in valid_selections :
                print("ERROR: please enter a valid chart type!\n")
            else:
                return chart_type
            
    def get_time_series(self):
        valid_selections = ["1", "2", "3", "4"]
        while True:
            self.printTimeSriesMenu()
            time_series_option = input("Enter time series option (1, 2, 3, 4): ")
            if not self.isValidString(time_series_option) or time_series_option not in valid_selections :
                print("ERROR: please enter a valid time series option!\n")
            else:
                return time_series_option

    def printChartMenu(self):
        print("\nChart Types\n-------------")
        print("1. Bar")
        print("2. Line\n")

    def printTimeSriesMenu(self):
        print("\nSelect the Time Series of the chart you want to Generate")
        print("--------------------------------------------------------")
        print("1. Intraday")
        print("2. Daily")
        print("3. Weekly")
        print("4. Monthly\n")

    def isValidString(self, the_string):
        if the_string == "":
            return False
        else:
            return True

    def get_date(self, period):
        prompt = f"Enter the {period} Date (YYYY-MM-DD): "
        date_regex = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$'
        
        while True:
            the_date = input(prompt)
            if re.match(date_regex, the_date):
                try:
                    #return the date as a date object
                    return datetime.strptime(the_date, "%Y-%m-%d")
                except ValueError as err:
                    print(f"ERROR: {str(err)}\n")

            else:
                print("ERROR: Enter the date in correct (YYYY-MM-DD) format! \n")

    def valid_date_range(self, start_date, end_date):
        if start_date >= end_date:
            print("ERROR: Start date cannot be later than end date. Enter the dates again.\n")
            return False
        else:
            return True

#HERE ARE THE FIVE UNIT TESTS THAT ARE SUPPOSED TO BE RAN

class UserInputTest(unittest.TestCase):
    #symbol: capitalized, 1-7 alpha characters
    def test_get_symbol_valid_input(self):
        user_input = UserInput()
        symbol = user_input.get_symbol()
        self.assertTrue(symbol.isalpha() and symbol.isupper())
        self.assertTrue(1 <= len(symbol) <= 7)

    #chart type: 1 numeric character, 1 or 2
    def test_get_chart_type_valid_input(self):
        user_input = UserInput()
        chart_type = user_input.get_chart_type()
        self.assertTrue(chart_type.isdigit())
        self.assertTrue(chart_type in ["1", "2"])

    #time series: 1 numeric character, 1 - 4
    def test_get_time_series_valid_input(self):
        user_input = UserInput()
        time_series = user_input.get_time_series()
        self.assertTrue(time_series.isdigit())
        self.assertTrue(time_series in ["1", "2", "3", "4"])

    #start date: date type YYYY-MM-DD
    def test_get_start_date_valid_input(self):
        user_input = UserInput()
        start_date = user_input.get_date('Start')
        self.assertIsInstance(start_date, datetime)

    #end date: date type YYYY-MM-DD
    def test_get_end_date_valid_input(self):
        user_input = UserInput()
        end_date = user_input.get_date('End')
        self.assertIsInstance(end_date, datetime)

#IF MAIN/NAME STATEMENT
if __name__ == '__main__':
    unittest.main()

"""
Henry Ang
CSC 4800 Advanced Python
1/12/17
Lab 2 - Calendar For A Year

This program prompts the user to enter a year and generates a calendar for that year into a output file.
Output filename: calendarYYYY.txt
"""

def createCalendar():
    """
    Creates a prompt to ask user to enter a year and writes the calendar for that year into a output file.
    """

    try:                                            # try-except to check if input is invalid

        year = int(input('Enter a year (YYYY): '))  # ask user to input year YYYY
        print()
        if (year < 1000) | (year > 9999):           # check if year is 4 digit, validates for negative numbers
            raise ValueError()

    except ValueError:
        print("Year must be a 4 digit number, please enter a 4 digit year (YYYY).")
        createCalendar()            # recall create calendar function


    month = ['January', 'February', 'March', 'April', 'May', 'June',
             'July', 'August', 'September', 'October', 'November', 'December']

    daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # days in each month, does not include leap year

    if isLeapYear(year) == True:           # checks if current year is a leap year
        daysInMonth[1] = 29

    dayOfWeek = dayOfWeekJan1(year) + 1    # given 0-6,
                                           # 1 = Sun, 2 = Mon, 3 = Tues, 4 = Wed, 5 = Thu, 6 = Fri, 7 = Sat

    filename = "calendar", year ,".txt"
    with open(str(filename), 'w') as outputfile:       # create output file

        for i in range(0, 12, 1):                      # loop for 12 months
            # prints to output file
            print('      ', month[i], year, file=outputfile)            # prints month, year
            print('Sun Mon Tue Wed Thu Fri Sat', file=outputfile)       # prints days of week
            print("    " * (dayOfWeek - 1) , end="", file=outputfile)   # prints spaces for 1st day of week

            for j in range(1, daysInMonth[i] + 1, 1): # prints all days in each month
                if (j > 9):                           # case for 2 digit number
                    print(j, " ", end="", file=outputfile)             # formatting for 2 digit number
                else:
                    print('', j, " ", end="", file=outputfile)         # formatting for 1 digit number

                if (dayOfWeek == 7):                  # if day of week is Saturday print new line
                    dayOfWeek = 0                     # resets week
                    if j != daysInMonth[i]:           # don't print new line if day is last day of month
                        print(file=outputfile)
                dayOfWeek += 1                        # sets day of week to Sunday(1)
            print(file=outputfile)
            print(file=outputfile)

    outputfile.close()

def isLeapYear(currentYear):
    """
    Determines if the current year is a leap year

    :param currentYear: User input of year
    :return bol: True or False
    """

    bol = False
    if ((int(currentYear) % 4 == 0) & (int(currentYear) % 100 != 0)) | (int(currentYear) % 400 == 0):
        bol = True

    return bol

def dayOfWeekJan1(currentYear):
    """
    Calculates the starting day of the week of January 1 of a year

    :param currentYear: User input of year
    :return int(x): Value of day of week 0-6
    """

    x = (int(currentYear) + ((int(currentYear) - 1 ) / 4) -
        ((int(currentYear) - 1) / 100 ) + ((int(currentYear) - 1) / 400)) % 7

    return int(x)

def main():
    """
    Main function of the program. Introduces the user to the program and calls create calendar.
    """

    print('Welcome to the Calendar Generator, written by Henry Ang.') # intro to program
    createCalendar()

if __name__ == "__main__":
    main()


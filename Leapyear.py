#-----------------program that checks if a year is a leap year--------------------


def is_leap_year(year):

    #It is divisible by 4 and not divisible by 100, or
    #It is divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
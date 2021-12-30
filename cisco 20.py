def is_year_leap(year):
   if year % 4 == 0:
        if year % 400 == 0:
            return True
        return year % 100 != 0
    return False
def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if isYearLeap(year):
            return 29
        else:
            return 28


print(days_in_month(2000, 12))
print(is_year_leap(2000))

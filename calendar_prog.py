import calendar

def calen(year,month):
    cal=calendar.TextCalendar(calendar.SUNDAY)
    cal1=cal.formatmonth(year,month)
    print(cal1)
    
year=int(input("Enter the year"))
month=int(input("Enter the month"))

calen(year,month)

# import calendar

# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))

# # Display Specific Month Calendar
# print(calendar.month(year, month))
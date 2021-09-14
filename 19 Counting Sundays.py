""" Problem 19
Start: Sep/14/2021 12:15pm
Finished: Sep/14/2021 7:20pm
"""

def convert_date(date):
    # convert "mm DD yyyy" to [mm, dd, yyyy]
    day, month, year = date.split(" ")
    MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return [int(day),MONTHS.index(month)+1,int(year)]

def days_in_month(month,year):
    # Feb has 29 on leap years, 28 on normal years
    if month == 2:
        # leap year occurs on years divisible by 4, but not on years divisible by 100 unless divisible by 400
        if (year % 100 or year % 400 == 0) and year % 4 == 0:
            return 29
        else:
            return 28
    # ["Apr","Jun","Sep","Nov"]
    THIRTY_DAYS = [4,6,9,11]
    # check if month has 30 or 31 days
    if month in THIRTY_DAYS:
        return 30
    else:
        return 31

def days_in_year(year):
    # leap year occurs on years divisible by 4, but not on years divisible by 100 unless divisible by 400
    if (year % 100 or year % 400 == 0) and year % 4 == 0:
        return 366
    return 365

def days_between(lower,upper):
    l_day, l_month, l_year = lower
    u_day, u_month, u_year = upper

    days = 0
    # cancel out days from equation
    days -= l_day
    days += u_day

    # cancel out months from equation
    days -= sum(days_in_month(month,l_year) for month in range(1,l_month))
    days += sum(days_in_month(month,u_year) for month in range(1,u_month))

    # add the days between the years
    days += sum(days_in_year(year) for year in range(l_year,u_year))
    return days

def compute(lower, upper):
    sundays = 0
    # convert "mm DD yyyy" to [mm, dd, yyyy]
    l_day, l_month, l_year = convert_date(lower)
    u_day, u_month, u_year = convert_date(upper)

    # 1/Jan/1900 is the given Monday
    MON_CONST = convert_date("1 Jan 1900")
    
    # loop thru all months from u_month,u_year to l_month,l_year
    for year in range(l_year,u_year+1):
        start_month = 1
        end_month = 12

        if year == l_year:
            start_month = l_month
        if year == u_year:
            end_month = u_month
        
        for month in range(start_month,end_month+1):
            # days_between%7+1 is the weekday(1=Mon,2=Tue,3=Wed,etc.) if equal to 7 is Sunday
            if days_between(MON_CONST,[1,month,year])%7+1 == 7:
                sundays += 1
    return sundays

start = "1 Jan 1901"
end = "31 Dec 2000"
print(f"The Number of Sundays That Fell on the First Month During the First Century Is: {compute(start,end)}")
import datetime

birth_year = int(input("Enter your birth year (YYYY): "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day (1-31): "))

today = datetime.date.today()

birth_date = datetime.date(birth_year, birth_month, birth_day)

age_in_days = (today - birth_date).days
age_in_years = age_in_days // 365

print("You are", age_in_years, "years old.")
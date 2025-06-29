import datetime

# Step 1: Take user input
birth_year = int(input("Enter your birth year (YYYY): "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day (1-31): "))

# Step 2: Get today's date
today = datetime.date.today()

# Step 3: Create birth date
birth_date = datetime.date(birth_year, birth_month, birth_day)

# Step 4: Calculate age
age_in_days = (today - birth_date).days
age_in_years = age_in_days // 365

# Step 5: Show result
print("You are", age_in_years, "years old.")
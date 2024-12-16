import datetime

# Get current date and time
current_datetime = datetime.datetime.now()
print(current_datetime)  # Output: 2024-12-15 12:30:45.123456

# Format date
formatted_date = current_datetime.strftime("%Y-%m-%d")
print(formatted_date)  # Output: 2024-12-15

# Calculate the difference between two dates
date1 = datetime.date(2024, 12, 15)
date2 = datetime.date(2025, 12, 15)
difference = date2 - date1
print(difference.days)  # Output: 366

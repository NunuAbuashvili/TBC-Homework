# დაწერეთ პროგრამა, რომელიც მიიღებს თარიღს. პროგრამამ თარიღი უნდა გადაიყვანოს განსხვავებულ ფორმატში და დაბეჭდოს ეკრანზე. Input: 2024-03-22T19:17:42.956376+00:00 Output: 22-03-2024 7:17:42 +0

# Ask user to enter a date in the given format, and remove leading and trailing whitespaces (if any) from the input
input_date = input("Please enter a date in the following format: [Year]-[Month]-[Day]T[hour]:[minute]:[second.ms][timezone]: ").strip()

# Parse date, time and timezone from the input
date = input_date[:input_date.find('T')]
time = input_date[input_date.find('T') + 1:input_date.find('.')]
timezone = input_date[-6:input_date.rfind(':')]

# Format date rearranging year, month and day
year = date[:date.find('-')]
month = date[date.find('-') + 1:date.rfind('-')]
day = date[-2:]

# Formatted date = day-month-year
output_date = day + '-' + month + '-' + year

# Format time using 12-hour format
hour = int(time[:time.find(':')])
minute_second = time[time.find(':') + 1:]
output_hour = ''

if hour == 00:
    output_hour = '12'
elif hour == 12:
    output_hour = '12'
else:
    output_hour = hour % 12

# Formatted time = hour (using 12-hour format):minute:second
output_time = str(output_hour) + ':' + minute_second

# Format timezone by removing leading zero
output_timezone = timezone.replace('0', '', 1)

# Combine formatted date, time and timezone
formatted_date = output_date + ' ' + output_time + ' ' + output_timezone

# Print the formatted date
print(formatted_date)

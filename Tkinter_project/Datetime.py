import datetime

date = datetime.date(2021, 11, 9)
current_date = datetime.datetime.now()  # get the current day with year, month, day, hour, minute, and second
msg = "Today is: {}"
if current_date.strftime("%Y-%m-%d") == str(date):
    print(msg.format(date))
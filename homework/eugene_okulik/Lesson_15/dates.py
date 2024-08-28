import datetime


now = datetime.datetime.now()
print(now)
today_midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
print(today_midnight)
after_midnight = now - today_midnight
print(after_midnight)
print(type(after_midnight))
print(after_midnight.days)
print(after_midnight.microseconds)
ten_days = datetime.timedelta(days=10)
in_ten_days = now + ten_days
print(in_ten_days)

birth = datetime.datetime.fromisoformat('1985-01-04 10:20:14.040155')
age = (now - birth)
print(age)
fifteen = now + datetime.timedelta(days=20)
print(fifteen)

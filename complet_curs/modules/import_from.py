from datetime import date

print(date.today())
print(date.weekday(date.today()))
print(date.isocalendar(date.today()))

print("40 days after today will be ",date.fromordinal(date.today().toordinal()+ 40))
_40days = date.fromordinal(date.today().toordinal()+ 40)
_today = date.today()
print(_40days - _today)
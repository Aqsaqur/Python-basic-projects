from datetime import date 

date1 = date(2025, 4, 7)

date2 = date(2025, 5, 10)

delta = date2 - date1

print(delta.days)

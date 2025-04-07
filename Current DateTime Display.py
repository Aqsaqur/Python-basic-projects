# Write a Python program to display the current date and time.Python certification
import datetime

today = datetime.datetime.now()

print("Current date and time : ")
print(today.strftime("%Y-%m-%d %H:%M:%S"))


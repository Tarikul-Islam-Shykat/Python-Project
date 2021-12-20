import datetime as dt

user_inpput = input("Enter your goal with a deadline ex: 12.5.2022 \n[date : month : year] : ")
deadLine = user_inpput

lastdate = dt.datetime.strptime(deadLine,"%d.%m.%Y") # formatting date

today_date = dt.datetime.today() # getting todays date

# to get the date time of todate

days_left = lastdate - today_date # days left


print(days_left.days,"days left")  #printing only the days left

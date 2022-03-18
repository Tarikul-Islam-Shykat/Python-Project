
from plyer import notification
import time as tm

# for time function
#print(now)  time.struct_time(tm_year=2022, tm_mon=3, tm_mday=18, tm_hour=20, tm_min=48, tm_sec=6, tm_wday=4, tm_yday=77, tm_isdst=0)

worked = False

while (worked == False):
    now  = tm.gmtime()
    #print("checking")
    hour = now[3]
    minute = now[4]
    if((hour == 20) and (minute == 59)):
        title =  "Drink water"
        message = "Its been 1 hour since you  last drank water"
        notification.notify(
            title = title,
            message = message,
            app_icon = "water.ico",
            timeout = 5,
            toast = False
        )
        break
    else:
        pass




# parameters
'''
title : Title of the notification
message : Message of the notification
app_name : Name of the app launching with the message
app_icon : Icon to be displayed along with the message   > https://icon-icons.com/ > download the ico file
timeout : time to display on the message for, defaults 10
ticker : text to display on the status bar as the notification arrives
toast : simple message instead of full notification

'''
# Documentation : https://plyer.readthedocs.io/en/latest/

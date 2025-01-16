import time
import datetime

#user's date and time
usr_date_input = input("Enter date in fomat(YY-MM-DD): ")
usr_time_input = input("Enter time in HH:MM: ")
formated_date = datetime.datetime.strptime(usr_date_input,"%Y-%m-%d")

formated_datetime = f"{formated_date.strftime('%Y-%m-%d')} {usr_time_input}:00.000000"
formated_datetime_obj = datetime.datetime.strptime(formated_datetime, "%Y-%m-%d %H:%M:%S.%f")
print(formated_datetime_obj)

#setting up alaram
while True:
    #Current time and date
    timinings = datetime.datetime.now()
    print(timinings)
    if timinings >= formated_datetime_obj:
        print("Alaram rings....")
        break

    time.sleep(1)



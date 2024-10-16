#medication reminder by adding exact date and time
#at first creating dictionary
medications=[

    {'name':'paracetamol','time':"8:00"}, # 8 am
    {'name':'ibuprofen','time': "12:00"}, # 12 am
    {'name':'Vitamin c','time': "19:00"}  # 7 pm

]
#function to check for medications and time
from datetime import datetime

def medication_reminder(medication_list):
    current_time = datetime.now().strftime("%H:%M")
    for medication in medication_list:
        if  medication['time'] == current_time:
            print(f"please take you medicine {medication['name']} ")

medication_reminder(medications)

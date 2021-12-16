import json
from datetime import datetime
from Function import GetClosest

f = open("data.json")
holidaylist = json.load(f)
f.close()
f = open("time.json")
timetable = json.load(f)
f.close()

print(GetClosest(timetable, holidaylist, datetime(2021, 12, 15, 1, 50)))
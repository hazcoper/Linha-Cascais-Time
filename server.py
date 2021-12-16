from flask import Flask
import datetime
import json

from Function import DealTime, GetClosest
 
app = Flask(__name__)




# Opening JSON file
f = open('data.json') 
holidaylist = json.load(f)
f.close()
f = open('time.json') 
timetable = json.load(f)
f.close()

# print(GetClosest(timetable, holidaylist, datetime.datetime(2021, 12, 20, 20, 15, 10)))

@app.route('/carcavelos-lisboa')
def helloHandler():
    return GetClosest(timetable,holidaylist)


app.run(host='0.0.0.0', port= 8090)
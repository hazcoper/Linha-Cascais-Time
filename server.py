from flask import Flask
import datetime
import json

from Function import DealTime, GetClosest
 
app = Flask(__name__)




# Opening JSON file
f = open('data.json') 
holiday = json.load(f)
f.close()
f = open('time.json') 
timetable = json.load(f)
f.close()



print(DealTime(datetime.datetime(2021, 12, 15, 1, 50), False))
print(GetClosest())

# @app.route('/carcavelos-lisboa')
# def helloHandler():
#     return str(GetClosest())


# app.run(host='0.0.0.0', port= 8090)



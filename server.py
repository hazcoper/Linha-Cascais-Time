from flask import Flask
import datetime
import json

 
app = Flask(__name__)



def IsWeekend(dtime):
    """
    return if given date is a weekend or not
    """

    return True if dtime.weekday() >= 6 else False   #returns the day of the week, 0 is monday


def IsHoliday(dtime):
    """
    returns if given date is a holiday or not
    """
    global holiday

    month = dtime.month
    day = dtime.day

    return (month in holiday and holiday[month] == day)





@app.route('/helloesp')
def helloHandler():
    return str(IsWeekend(datetime.date.today()))

# Opening JSON file
f = open('data.json') 
holiday = json.load(f)
f.close()
 
print(IsWeekend(datetime.date.today()))
print(IsHoliday(datetime.date.today()))

app.run(host='0.0.0.0', port= 8090)



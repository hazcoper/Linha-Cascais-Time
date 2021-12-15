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



def DealTime(time, isholiday):
    """
    time is in hh:mm
    Receive a time and a holiday flag and return how many minutes until the next train
    """
    global timetable
    
    hour = time.split(":")[0]
    minute = time.split(":")[1]
    print(f"This is the hour {hour}:{minute}")

    if isholiday:
        flag = "f"
    else:
        flag = "n"

    option1 = timetable[flag][hour]
    print(f"This is the {option1}")
    minOp1 = ""
    for temp in option1:
        if int(minute) <= int(temp):
            minOp1 = temp
            break
    
    if minOp1 == "":
        hour = str((int(hour) + 1) %24)
        # print(f"This is the closest --> {hour}:{timetable[flag][hour][0]}")
        return (int(minute)-int(timetable[flag][hour][0]))%60
    else:
        # print(f"This is the closest --> {hour}:{minOp1}")
        return int(minOp1)-int(minute)

def GetClosest():
    """
    Returns the closest train using all the variables above
    """
    mydate = datetime.datetime.now()
    mytime = f"{mydate.hour}:{mydate.minute}"

    if IsHoliday(mydate) or IsWeekend(mydate):
        return DealTime(mytime, True)
    
    return DealTime(mytime, False)


# Opening JSON file
f = open('data.json') 
holiday = json.load(f)
f.close()
f = open('time.json') 
timetable = json.load(f)
f.close()



@app.route('/carcavelos-lisboa')
def helloHandler():
    return str(GetClosest())


app.run(host='0.0.0.0', port= 8090)



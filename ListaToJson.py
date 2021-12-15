
"""
convert lista de feriados no wanted JSON
no formato:
day-month
day-month....
"""

import json


def Feriados():
    f = open("ListaFeriados", "r")

    myDict = {}

    for line in f.readlines():
        myvalue = line.split("\n")[0].split("-")

        if myvalue[1] in myDict:
            myDict[myvalue[1]].append(myvalue[0])
        else:
            myDict[myvalue[1]] = [myvalue[0]]

    print(myDict)

    with open('data.json', 'w') as fp:
        json.dump(myDict, fp)


    f.close()

def Timetables():
    """
    get the timetable in a raw format from the file and convert it to json
    """
    station = "Carcavelos"
    f = open(station, "r")

    myDict = {}
    flag = "none"
    for line in f.readlines():
        print("this is the line ", line)
        if line == "normal:\n":
            flag = "n"
            myDict[flag] = {}
        elif line == "feriados:\n":
            flag = "f"
            myDict[flag] = {}
            print("f flag was added")
        else:
            timeList = line.split(" ")
            for time in timeList:

                hour = time.split(":")[0]
                minute = time.split(":")[1]
                if "\n" in minute:
                    minute = minute[:-1]
                if hour not in myDict[flag]:
                    myDict[flag][hour] = [minute]
                
                else:
                    myDict[flag][hour].append(minute)
    
    with open('time.json', 'w') as fp:
        json.dump(myDict, fp)



    f.close()

Timetables()
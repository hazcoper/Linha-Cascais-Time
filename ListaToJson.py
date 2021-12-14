
"""
convert lista de feriados no wanted JSON
no formato:
day-month
day-month....
"""

import json


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
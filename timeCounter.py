#! /usr/bin/env python

def extractTimeFromString(timeVal):
    if timeVal == '':
        return (0, 0)

    if ':' not in timeVal:
        return (0, int(timeVal))
    
    hours = timeVal.split(':')[0]
    minutes = timeVal.split(':')[1]

    if hours[0] == '0':
        hours = hours[1 : : ]

    if minutes[0] == '0':
        minutes = minutes[1 : : ]

    minutes = int(minutes)
    hours = int(hours)

    return (hours, minutes)

def extractTime(timeLine):
    timeVals = timeLine.split(' ')
    timeValList = []
    for timeVal in timeVals:
        timeValList.append(extractTimeFromString(timeVal))

    return timeValList

def countTime(timeLine):
    if len(timeLine) == 0:
        return (0, 0)

    timeList = extractTime(timeLine)

    totalHours = 0
    totalMinutes = 0
    for timeVal in timeList:
        totalHours += timeVal[0]
        totalMinutes += timeVal[1]

    # Might be more that 60 mins in totalMinutes
    while totalMinutes >= 60:
        totalMinutes -= 60
        totalHours += 1

    print("Total hours:", totalHours)
    print("Total Minutes:", totalMinutes)

    return (totalHours, totalMinutes)

def addPrevTotal(prevTotal, currentSessionTotal):
    newTotalHours = prevTotal[0] + currentSessionTotal[0]
    newTotalMinutes = prevTotal[1] + currentSessionTotal[1]

    while newTotalMinutes >= 60:
        newTotalMinutes -= 60
        newTotalHours += 1

    return (newTotalHours, newTotalMinutes)
    

            
def main():
    totalTimeLineIndicies = []
    timeTrackLineIndicies = []
    prevTotals = []
    tempIndex = 0

    with open("study_times.txt", 'r') as txt:
        totalTimes = []
        lines = txt.readlines()

        for line in lines:
            if line[0] == '*':
                line = line.strip('\n')
                totalTimes.append(countTime(line[1:]))
                timeTrackLineIndicies.append(tempIndex)
                
            if line[:6] == "Total:" :
                line = line.strip('\n')
                line = line.strip(' ')
                prevTotals.append(extractTimeFromString(line[6:]))
                totalTimeLineIndicies.append(tempIndex)
            
            tempIndex += 1

    for i in range(len(totalTimes)):
        totalTimes[i] = addPrevTotal(prevTotals[i], totalTimes[i])
            
    tempIndex = 0
    for index in totalTimeLineIndicies:
        lines[index] = "Total: " + str(totalTimes[tempIndex][0]) + ':' + str(totalTimes[tempIndex][1])
        tempIndex += 1

    for index in timeTrackLineIndicies:
        lines[index] = "*"


    with open("study_times.txt", 'w') as txt:
        for line in lines:
            if '\n' not in line:
                line = line + '\n'
            txt.write(line)

if __name__ == "__main__":
    main()
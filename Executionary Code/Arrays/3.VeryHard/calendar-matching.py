# Time complexity: O(c1 + c2)
# Space complexity: O(c1 + c2)
def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    updatedCalendar1 = updateCalendar(calendar1, dailyBounds1)
    updatedCalendar2 = updateCalendar(calendar2, dailyBounds2)

    mergedCalendar = mergeCalendars(updatedCalendar1, updatedCalendar2)
    return getFreeIntervals(mergedCalendar, meetingDuration)


def updateCalendar(calendar, dailyBounds):
    outCalendar = calendar[:]
    outCalendar.insert(0, ["0:00", dailyBounds[0]])
    outCalendar.append([dailyBounds[1], "23:59"])
    return list(map(lambda m: [convertTimeToMinutes(m[0]), convertTimeToMinutes(m[1])], outCalendar))


def convertTimeToMinutes(time):
    hours, minutes = list(map(int, time.split(':')))
    return hours * 60 + minutes


def mergeCalendars(calendar1, calendar2):
    outArr = []
    i, j = 0, 0

    increaseValue = "null"
    while i < len(calendar1) or j < len(calendar2):
        if increaseValue == "i" or (not increaseValue == "j" and calendar1[i][0] <= calendar2[j][0]):  # and
            captureOverlapingIntervals(outArr, calendar1[i], i, j)
            i += 1

            if i == len(calendar1):
                increaseValue = "j"

        else:
            captureOverlapingIntervals(outArr, calendar2[j], i, j)
            j += 1

            if j == len(calendar2):
                increaseValue = "i"
    return outArr


def captureOverlapingIntervals(outArr, newCalendarInterval, i, j):
    if i == 0 and j == 0:
        outArr.append(newCalendarInterval)
        return

    x = len(outArr) - 1
    if outArr[x][1] >= newCalendarInterval[0]:
        outArr[x][1] = max(outArr[x][1], newCalendarInterval[1])
    else:
        outArr.append(newCalendarInterval)


def getFreeIntervals(mergedCalendar, meetingDuration):
    outArr = []
    for i in range(len(mergedCalendar) - 1):
        currentInterval = [mergedCalendar[i][1], mergedCalendar[i + 1][0]]
        amountOfMeetings = (currentInterval[1] - currentInterval[0]) // meetingDuration

        if amountOfMeetings >= 1:
            # currentInterval[1] = currentInterval[0] + (amountOfMeetings * meetingDuration)
            outArr.append(convertMinutesToTime(currentInterval))
    return outArr


def convertMinutesToTime(minutesInterval):
    # startTime = list(map(lambda b: str(b // 60) + ":" + str(b % 60), minutesInterval))
    startTime = list(map(lambda b: str(b // 60) + ":" + str(b % 60) if b % 60 >= 10 else str(b // 60) + ":" + str("0") + str(b % 60), minutesInterval))
    return startTime


def runTestCases():
    print(calendarMatching(
    [
        ["9:00", "10:30"],
        ["12:00", "13:00"],
        ["16:00", "18:00"]
    ],
    ["9:00", "20:00"],
    [
        ["10:00", "11:30"],
        ["12:30", "14:30"],
        ["14:30", "15:00"],
        ["16:00", "17:00"]
    ],
    ["10:00", "18:30"],
    30))
    # Expected output:
    # [
    #     ["11:30", "12:00"],
    #     ["15:00", "16:00"],
    #     ["18:00", "18:30"]
    # ]


    print(calendarMatching(
    [
        ["8:00", "10:30"],
        ["11:30", "13:00"],
        ["14:00", "16:00"],
        ["16:00", "18:00"]
    ],
    ["8:00", "18:00"],
    [
        ["10:00", "11:30"],
        ["12:30", "14:30"],
        ["14:30", "15:00"],
        ["16:00", "17:00"]
    ],
    ["7:00", "18:30"],
    15))
    # Expected output: []


runTestCases()
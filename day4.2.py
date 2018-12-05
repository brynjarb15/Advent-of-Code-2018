
class Timestamp:
    def __init__(self, m, d, h, min, e):
        self.month = m
        self.day = d
        self.hour = h
        self.minute = min
        self.event = e

    def __repr__(self):
        string = "\nmonth: " + str(self.month) + "\nday: " + str(self.day) + "\nhour: " + str(self.hour) + "\nminute: " + str(
            self.minute) + "\nevent: " + str(self.event) + "\n------------\n"
        return string


class sleepTime:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.duration = end-begin

    def __repr__(self):
        return str(self.duration)

#[1518-09-29 00:35] falls asleep
SLEEP = 'falls asleep'
WAKE_UP = 'wakes up'
BEGIN_SHIFT = 'begins shift'

f = open('inputs/day4-input.txt', 'r')

allTimestamps = f.read().split('\n')


allTimestamps = [
    '[1518-11-03 00:05] Guard #10 begins shift',
    '[1518-11-03 00:29] wakes up',
    '[1518-11-01 00:05] falls asleep',
    '[1518-11-01 00:25] wakes up',
    '[1518-11-02 00:40] falls asleep',
    '[1518-11-05 00:55] wakes up',
    '[1518-11-01 00:30] falls asleep',
    '[1518-11-01 00:55] wakes up',
    '[1518-11-02 00:50] wakes up',
    '[1518-11-03 00:24] falls asleep',
    '[1518-11-04 00:02] Guard #99 begins shift',
    '[1518-11-04 00:36] falls asleep',
    '[1518-11-04 00:46] wakes up',
    '[1518-11-05 00:03] Guard #99 begins shift',
    '[1518-11-01 00:00] Guard #10 begins shift',
    '[1518-11-05 00:45] falls asleep',
    '[1518-11-01 23:58] Guard #99 begins shift'
    
]
#Remove the year and other stuff
allTimestamps = [t.replace('[1518-', '') for t in allTimestamps]
allTimestamps = [t.replace(']', '') for t in allTimestamps]

timestampObjects = []
#Make the objects
for stamp in allTimestamps:
    date, time, event = stamp.split(' ', 2)
    month, day = date.split('-')
    hour, minute = time.split(':')
    newStamp = Timestamp(int(month), int(day), int(hour), int(minute), event)
    timestampObjects.append(newStamp)

#Sort the list
timestampObjects.sort(key=lambda x: x.minute)
timestampObjects.sort(key=lambda x: x.hour)
timestampObjects.sort(key=lambda x: x.day)
timestampObjects.sort(key=lambda x: x.month)

currentId = -1
lastSleep = -1

#Initalize minutes with all 0
minutes = {}
for i in range(60):
    minutes[i] = 0

guards = {}
guardsMinutes = {}
for stamp in timestampObjects:
    if stamp.event.endswith(BEGIN_SHIFT):
        currentId = int(stamp.event.split(' ')[1].replace('#', ''))
        if not currentId in guards:
            guards[currentId] = []
            guardsMinutes[currentId] = minutes.copy()
    if stamp.event == SLEEP:
        lastSleep = stamp.minute
    if stamp.event == WAKE_UP:
        guards[currentId].append(sleepTime(lastSleep, stamp.minute))


# Get the guard that sleeps most
mostTimeId = -1
largestSoFarSum = -1
for g in guards:
    sum = 0
    for time in guards[g]:
        sum += time.duration
    if sum > largestSoFarSum:
        mostTimeId = g
        largestSoFarSum = sum






#Put values on all minutes
for g in guardsMinutes:
    for sleep in guards[g]:
        start = sleep.begin
        end = sleep.end
        while start < end:
            guardsMinutes[g][start] += 1
            #minutes[start] += 1
            start += 1

print(guardsMinutes)
#Get the largest minute
largestId = -1
largestCount = -1
largestMinute = -1
for g in guardsMinutes:
    for minute in guardsMinutes[g]:
        if guardsMinutes[g][minute] > largestCount:
            largestId = g
            largestCount = guardsMinutes[g][minute]
            largestMinute = minute

print('Guard id:', largestId)
print('Minute:', largestMinute)
print('Multi:', largestId * largestMinute) # answer 47910





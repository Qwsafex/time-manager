from collections import defaultdict


def collectStatistics(statFile):
    curline = statFile.readline()
    activities = defaultdict(int)
    while curline != "":
        parts = curline.split('|')
        if len(parts) == 4:
            activities[parts[2]] += int(parts[3])
        curline = statFile.readline()
    return activities


def statisticsText(statDict):
    total = 0
    statisticsText = ""
    for key, value in sorted(statDict.items(), key=lambda x: -x[1]):
        value = int(value)
        total += value
        hours = value // 3600
        minutes = (value % 3600) // 60

        if hours > 0:
            statisticsText += "{0} for {1} hours and {2} minutes\n".format(
                                                    key, hours, minutes)
        else:
            statisticsText += "{0} for {1} minutes\n".format(key, minutes)
    hours = total // 3600
    minutes = (total % 3600) // 60
    if hours > 0:
        statisticsText += "Total: {0} hours {1} minutes".format(hours,
                                                                minutes)
    else:
        statisticsText += "Total: {0} minutes".format(minutes)
    return statisticsText

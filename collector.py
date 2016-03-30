from collections import defaultdict

with open("time-manager-log.txt") as f:
	curline = f.readline()
	activities = defaultdict(int)
	while curline != "":
		parts = curline.split('|')
		activities[parts[1]] += int(parts[2])
		#print(curline, "###")
		curline = f.readline()

	res = []
	total = 0
	for key, value in sorted(activities.items(), key=lambda x: -x[1]):
		value = int(value)
		total += value
		hours = value // 3600
		minutes = (value%3600) // 60

		if hours > 0:
			print(key, "for", hours, "hours and", minutes, "minutes")
		else:
			print(key, "for", minutes, "minutes")
	hours = total // 3600
	minutes = (total%3600) // 60
	print(hours, minutes)
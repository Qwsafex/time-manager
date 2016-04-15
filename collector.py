from collections import defaultdict
import sys

with open(sys.argv[1]) as f:
	curline = f.readline()
	activities = defaultdict(int)
	while curline != "":
		parts = curline.split('|')
		#print(parts)
		activities[parts[2]] += int(parts[3])
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
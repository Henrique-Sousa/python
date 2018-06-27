import re

def time_to_list(s):
	s2 = s.split(':')
	t = s2[2].split(',')
	s2[2] = t[0]
	s2.append(t[1])
	return s2

def time_to_milisecs(t):
	return int(t[0])*3600000 + int(t[1])*60000 + int(t[2])*1000 + int(t[3]) 

def milisecs_to_time(milliseconds):
	hours, milliseconds = divmod(milliseconds, 3600000)
	minutes, milliseconds = divmod(milliseconds, 60000)
	seconds = float(milliseconds) / 1000
	s = "%i:%02i:%06.3f" % (hours, minutes, seconds)
	return s

def adjust(time, offset):
	t_i_conv = time_to_list(time)
	t_i_mili = time_to_milisecs(t_i_conv)
	t_i_updated = t_i_mili + offset
	return milisecs_to_time(t_i_updated)

## example
offset = -54*1000
name = "Silicon.Valley.S05E02.1080p.HEVC.x265-MeGusta.srt"
file = open(name, "r")
file2 = open("subtitle.srt", "w")
##

s1 = file.read()
l_num = s1.split('\n\n')
subtitle = []

for i in l_num:
	l_parts = i.split('\n')
	l_temp = l_parts[1].split("-->")
	t_start = l_temp[0].strip()
	t_start = adjust(t_start, offset)
	t_end = l_temp[1].strip()
	t_end = adjust(t_end, offset)
	l_temp2 = [t_start,t_end]
	l_parts[1] = l_temp2

	file2.write(l_parts[0]+"\n")
	adjusted_time = " -->  ".join(l_parts[1])
	file2.write(adjusted_time+"\n")
	for j in range(2,len(l_parts)):
		file2.write(l_parts[j]+"\n")
	file2.write("\n")
	
file2.close()
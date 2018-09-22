import os
import fileinput

# file = "/home/mariajesus/ownCloud/UOC/2018-19_Sem01/calendarUOC_v02.ics"

# fileHandler = open(file, "r")

# for line in fileHandler:
# 	if  "Mercado" in line:
# 		fileinput.lineno()
# 		print(line)
file = open("C:\\Users\\mjm\\ownCloud\\UOC\\2018-19_Sem01\\calendarUOC_v02.ics", "r")
for line_no, line in enumerate(file):
	if "TGCO" in line:
		print(str(line_no + 1) + " " + line)
file.close()
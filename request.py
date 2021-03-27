import PySimpleGUI as sg
import sys

sg.theme("Black")
layout = [
	[sg.Text("Save spotted! What change was that now?")],
	[sg.Button("Major"), sg.Button("Minor"), sg.Button("Patch"), sg.Button("None")]]

window = sg.Window(sys.argv[1], layout)

def update(event):
	if event == "None":
		return
	with open("data.db") as database:
		content = database.readlines()
	for line in content:
		if line.startswith(sys.argv[1]):
			line_index = content.index(line)
			version = line.split()[-1]
			version = version.strip()
			ver_length = len(version)
			version = version.split('.')
			version = [int(i) for i in version]
			if event == "Major":
				version[0] += 1
				version[1] = 0
				version[2] = 0
			if event == "Minor":
				version[1] += 1
				version[2] = 0
			if event == "Patch":
				version[2] += 1
			version = [str(i) for i in version]
			version = '.'.join(version)
			sg.popup(version)
			content[line_index] = line[:-ver_length-1] + version + "\n"
	with open("data.db","w") as database:
		for line in content:
			database.write(line)

while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED:
		break
	if event in ("Major", "Minor", "Patch", "None"):
		update(event)
		break

window.close()

import PySimpleGUI as sg
import sys

sg.theme("Black")
layout = [
	[sg.Text("Project Name", font="Lato 12")],
	[sg.Input(size=(34,1))],
	[sg.Button("Use", font="Lato 11"), sg.Button("Add", font="Lato 11"), sg.Button("Delete", font="Lato 11")]
]

window = sg.Window("UpdateGuard 0.5.0", layout)

while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED:
		break
	if event == "Use":
		with open(f"{sys.argv[1]}.key","w") as key:
			key.write(values[0])
		break
	if event == "Add":
		add_layout = [
			[sg.Text("Current Version", font="Lato 12")],
			[sg.Input(size=(34,1))],
			[sg.Button("OK", font="Lato 11")]
		]
		add_window = sg.Window(values[0], add_layout)
		while True:
			event, add_values = add_window.read()
			if event == sg.WIN_CLOSED:
				break
			if event == "OK":
				break
		add_window.close()
		with open("data.db","a") as database:
			database.write(f"{values[0]} {add_values[0]}\n")
		break
	if event == "Delete":
		with open("data.db") as database:
			data = database.readlines()
		with open("data.db","w") as database:
			for line in data:
				if not line.startswith(values[0]):
					database.write(line)
		break

window.close()

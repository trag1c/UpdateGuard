import os
import keyboard
from random import choice
from time import sleep

class UpdateGuard:
	def __init__(self):
		os.chdir("Python")
		os.chdir("UpdateGuard")
		self.tempid()

	def tempid(self):
		chars = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.tempid = "".join([choice(chars) for _ in range(4)])

	def init(self):
		with open(f"{self.tempid}.key","w") as _:
			pass
		os.system(f"python init.py {self.tempid}")
	
	def delete_key(self):
		try: os.remove(f"{self.tempid}.key")
		except: pass

	def request(self):
		with open(f"{self.tempid}.key") as key:
			project_name = key.read()
		os.system(f"python request.py {project_name}")

	def listen(self):
		while True:
			if keyboard.is_pressed("Ctrl+S"):
				sleep(0.5)
				self.request()
			if keyboard.is_pressed("Ctrl+Alt+End"):
				sleep(0.5)
				self.delete_key()
				break

ug = UpdateGuard()
ug.init()
ug.listen()

import sqlite3
import yaml
import re
from datetime import datetime
import time
import schedule
import subprocess
import psutil
#Write stuff to check the test db and do the flow chart

def init_rem_db():
	con = sqlite3.connect("Stores/reminders.db")
	cur = con.cursor()
	res = cur.execute("SELECT name FROM sqlite_master")
	for i in res.fetchall():
		cur.execute(f"DROP TABLE {i[0]}")
	cur.execute("CREATE TABLE reminders(start, day, duration, catagory)")
	cur.execute("INSERT INTO reminders VALUES (:null, 'MONDAY', :null, :null), (:null, 'TUESDAY', :null, :null), (:null, 'WEDNESDAY', :null, :null), (:null, 'THURSDAY', :null, :null), (:null, 'FRIDAY', :null, :null), (:null, 'SATURDAY', :null, :null), (:null, 'SUNDAY', :null, :null)", {"null": None})
	con.commit()


def write_to_rem_db(day: str, start:str, dur:str, cat:str):
	#verify
	con = sqlite3.connect("Stores/reminders.db")
	cur = con.cursor()
	if not re.search("^(MONDAY|TUESDAY|WEDNESDAY|THURSDAY|FRIDAY|SATURDAY|SUNDAY)$", day):#Chat GPT
		return 1
#	elif mod == "start":
#		if not re.search("^(?:[01]\d|2[0-3]):[0-5]\d$", val): #Check chatgpt for referncing
#			return 2
#		cur.execute(f"""UPDATE reminders 
#		SET start = '{val}'
#		WHERE day = '{day}'""")
#		con.commit()
#	elif mod == "duration":
#		if not val.isnumeric():
#			return 2
#		cur.execute(f"""UPDATE reminders
#		SET duration = {int(val)}
#		WHERE day = '{day}'""")
#		con.commit()
#	elif mod == "catagory":
#		cur.execute(f"""UPDATE reminders
#		SET catagory = '{val}'
#		WHERE day = '{day}'""")
#		con.commit()
#	
	if not re.search("^(?:[01]\d|2[0-3]):[0-5]\d$", start): #Check chatgpt for referncing
		return 2
	cur.execute(f"""UPDATE reminders 
	SET start = '{start}'
	WHERE day = '{day}'""")


	cur.execute(f"""UPDATE reminders
	SET duration = {float(dur)}
	WHERE day = '{day}'""")

	cur.execute(f"""UPDATE reminders
	SET catagory = '{cat}'
	WHERE day = '{day}'""")
	con.commit()
#
	return 0

def prevent_apps():
	if "steam.exe" in (i.name() for i in psutil.process_iter()):
		subprocess.call("TASKKILL /F /IM steam.exe", shell=True)




def read_fr_rem_db(day):
	#Return
	con = sqlite3.connect("Stores/reminders.db")
	cur = con.cursor()
	res = cur.execute(f"SELECT * FROM reminders")
	return res.fetchall()

			


def init_past_db():

	con = sqlite3.connect("Stores/past.db")
	cur = con.cursor()
	res = cur.execute("SELECT name FROM sqlite_master")
	for i in res.fetchall():
		cur.execute(f"DROP TABLE {i[0]}")
	cur.execute("CREATE TABLE past(start, day, duration, catagory, isfinished, actual_duration, week)")
	con.commit()


def send_to_past_db(day, act_time: int, is_finished: bool):
	con = sqlite3.connect("Stores/reminders.db")
	cur = con.cursor()
	res = cur.execute(f"SELECT * FROM reminders WHERE day = '{day}'")
	x = res.fetchone()
	for i in x:
		print(i)
		if i == None:
			return f"Cannot add None Value: {res.fetchall()[0]}"
	#Send
	send_con = sqlite3.connect("Stores/past.db")
	send_cur = send_con.cursor()
	is_finished = int(is_finished)
	week = send_cur.execute("SELECT MAX(week) FROM past")
	if week.fetchone()[0] == None:
		return "No vals in past"
	week = int(week.fetchone()[0])
	if day == 'MONDAY':
		week+=1

	print(week)
	res = cur.execute(f"SELECT * FROM reminders WHERE day = '{day}'")
	print(res.fetchone())
	send_cur.execute(f"INSERT INTO past VALUES ('{x[0]}', '{x[1]}', {x[2]}, '{x[3]}', {is_finished}, {act_time}, {week})")	
	send_con.commit()


	#Find Top Week
	"""send_res = send_cur.execute(f"SELECT MAX(week) FROM past")"""
	#print(send_res.fetchall()[0][0])



	"""x = None 
	for i in send_res.fetchall():
		if i[0] == None:
			break
		x = i[0]#Writing if caused issues, this works? WHY???????????????????
		break
	if x == None:
		return "No week found"
	last_day = send_cur.execute(f"""
	"SELECT day FROM past WHERE week = {x}"
	""")	
	#get most recent day in db
	max_day = -1
	for i in last_day.fetchall():
		print(time.strptime(i[0].lower(), '%A').tm_wday)
		if max_day <  time.strptime(i[0].lower(), '%A').tm_wday:
			max_day=time.strptime(i[0].lower(), '%A').tm_wday
	#If it is a new week the day should be """
	



def read_fr_past_db():
	#Send
	con = sqlite3.connect("Stores/past.db")
	cur = con.cursor()
	res = cur.execute(f"SELECT * FROM past")
	return res.fetchall()

def get_settings():
	with open("Stores/UI.yaml") as f:
		return yaml.safe_load(f)
def set_settings():
	pass 

def set_weekly():
	pass

def get_weekly():
	with open("Stores/WeeklyGoal.yaml") as f:
		return yaml.safe_load(f)
	
def init_setting():
	with open("Stores/UI.yaml", "w") as f:
		init_state = "UI:\n  theme:light"
		f.write(init_state)

def init_Weekly():
	with open("Stores/WeeklyGoal.yaml", "w") as f:
		weekly_state = "Weekly:\n  goal:None\n  succeed:[]\n\nCurrent_week:\n  goals:\n    - Monday:0\n    - Tuesday:0\n    - Wednesday:0\n    - Thusday:0\n    - Friday:0\n    - Saturday:0\n    - Sunday:0"
		f.write(weekly_state)

def update_rem_db():
	today = datetime.now().weekday()
	con = sqlite3.connect("src/Stores/reminders.db")
	cur = con.cursor()
	res = cur.execute("SELECT day FROM test")
	#:print(list(res.fetchall())[0:-1][1][0])
	day = None
	for e, i in enumerate(list(res.fetchall())[0:-1]):
		i=i[0]	
		#print(i)
		if i == "MONDAY":
			day = 0
		elif i == "TUESDAY":
			day = 1
		elif i == "WEDNESDAY":
			day = 2
		elif i == "THURSDAY":
			day = 3
		elif i == "FRIDAY":
			day = 4
		elif i == "SATURDAY":
			day = 5
		elif i == "SUNDAY":
			day = 6
		#print(day)
		if day > today:
			stat = get_weekly()	
			x = stat['Current_week']["goals"][e]
			time = float(x[x.find(':')+1::])
			#Yea this is big brain hours tbh
			cur.execute("")

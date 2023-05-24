import sqlite3
import yaml
import re
from datetime import datetime
#Write stuff to check the test db and do the flow chart

def init_rem_db():
	con = sqlite3.connect("./src/Stores/reminders.db")
	cur = con.cursor()
	res = cur.execute("SELECT name FROM sqlite_master")
	for i in res.fetchall():
		cur.execute(f"DROP TABLE {i[0]}")
	cur.execute("CREATE TABLE reminders(start, day, duration, catagory)")
	cur.execute("INSERT INTO reminders VALUES (:null, 'MONDAY', :null, :null), (:null, 'TUESDAY', :null, :null), (:null, 'WEDNESDAY', :null, :null), (:null, 'THURSDAY', :null, :null), (:null, 'FRIDAY', :null, :null), (:null, 'SATURDAY', :null, :null), (:null, 'SUNDAY', :null, :null)", {"null": None})
	con.commit()


def write_to_rem_db(day: str, mod: str, val: str):
	#verify
	con = sqlite3.connect("./src/Stores/reminders.db")
	cur = con.cursor()
	if not re.search("^(MONDAY|TUESDAY|WEDNESDAY|THURSDAY|FRIDAY|SATURDAY|SUNDAY)$", day):#Chat GPT
		return 1
	elif mod == "start":
		if not re.search("^(?:[01]\d|2[0-3]):[0-5]\d$", time): #Check chatgpt for referncing
			return 1
		cur.execute(f"""UPDATE reminder 
		SET start = {val}
		WHERE day = '{day}'""")
		con.commit()
	elif mod == "duration":
		if not val.isnumeric():
			return 1
		cur.execute(f"""UPDATE reminders
		SET duration = {int(val)}
		WHERE day = '{day}'""")
		con.commit()
	elif mod == "catagory":
		cur.execute(f"""UPDATE reminders
		SET catagory = '{val}'
		WHERE day = '{day}'""")
		con.commit()


def read_fr_rem_db():
	#Return
	con = sqlite3.connect("./src/Stores/reminders.db")
	cur = con.cursor()
	res = cur.execute("SELECT * FROM reminders")
	return res.fetchall()

			


def init_past_db():

	con = sqlite3.connect("./src/Stores/past.db")
	cur = con.cursor()
	res = cur.execute("SELECT name FROM sqlite_master")
	for i in res.fetchall():
		cur.execute(f"DROP TABLE {i[0]}")
	cur.execute("CREATE TABLE past(start, day, duration, catagory, isfinished, actual_duration)")
	con.commit()


def send_to_past_db(day,mod,val):
	#Verify
	
	#Send
	pass

def read_fr_past_db():
	#Send
	pass

def get_settings():
	with open("./src/Stores/UI.yaml") as f:
		return yaml.safe_load(f)
def set_settings():
	pass 

def set_weekly():
	pass

def get_weekly():
	with open("./src/Stores/WeeklyGoal.yaml") as f:
		return yaml.safe_load(f)
	
def init_setting():
	with open("./src/Stores/UI.yaml", "w") as f:
		init_state = "UI:\n  theme:light"
		f.write(init_state)

def init_Weekly():
	with open("./src/Stores/WeeklyGoal.yaml", "w") as f:
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

init_setting()
init_Weekly()
init_rem_db()
init_past_db()
write_to_rem_db("WEDNESDAY", "catagory", "math")
#update_rem_db()
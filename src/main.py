import sqlite3
import yaml
#Write stuff to check the test db and do the flow chart
def write_to_rem_db(time, day, sub, duration):
	#verify
	#Send
	pass

def read_fr_rem_db():
	#Return
	pass

def update_rem_db():
	pass

def send_to_past_db():
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
		weekly_state = "Weekly:\n  goal:null\n  succeed:[]"
		f.write(weekly_state)

init_setting()
print(get_settings())
init_Weekly()
print(get_weekly())
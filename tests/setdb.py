import sqlite3

def load_vals():
	con = sqlite3.connect("test.db")
	cur = con.cursor()
	cur.execute("DROP TABLE reminder")
	cur.execute("CREATE TABLE reminder(start, day, duration, finished, actual_time)")
	res = cur.execute("SELECT name FROM sqlite_master")
	print(res.fetchone())
	cur.execute("""
	INSERT INTO reminder VALUES
 	('13:00', Sat, 1, 1, 0.5),
	('13:00', 'Sun', 1.5, 1, 1.5),
	('17:00', 'Mon', 1.0, 0, NULL),
	('17:30', 'Tue', 0.5, 0, NULL)
	""")
	con.commit()

def pop_past_db():
	con = sqlite3.connect("../src/Stores/past.db")
	cur = con.cursor()
	#start, day, duration, catagory, isfinished, actual_duration, week
	cur.execute("""INSERT INTO past VALUES ('15:00', 'WEDNESDAY', 1.5, 'math', 1, 1, 1),
 ('15:00', 'WEDNESDAY', 1.5, 'math', 1, 1, 2),
 ('15:00', 'THURSDAY', 1.5, 'math', 1, 1, 2),
 ('15:00', 'FRIDAY', 1.5, 'math', 1, 1, 2),
 ('15:00', 'SUNDAY', 1.5, 'math', 1, 1, 3),
 ('15:00', 'WEDNESDAY', 1.5, 'math', 1, 1, 3),
 ('15:00', 'FRIDAY', 1.5, 'math', 1, 1, 3),
 ('15:00', 'SATURDAY', 1.5, 'math', 1, 1, 3),
 ('15:00', 'FRIDAY', 1.5, 'math', 1, 1, 4),
 ('15:00', 'WEDNESDAY', 1.5, 'math', 1, 1, 4),
 ('15:00', 'WEDNESDAY', 1.5, 'math', 1, 1, 5),
 ('15:00', 'WEDNESDAY', 1.5, 'math', 1, 1, 5)
 """)
	#SATURDAY IS THE LAST DAY
pop_past_db()
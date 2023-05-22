import sqlite3
con = sqlite3.connect("test.db")
cur = con.cursor()

cur.execute("DROP TABLE reminder")
cur.execute("CREATE TABLE reminder(start, day, duration, finished, actual_time)")
res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchone())
cur.execute("""
INSERT INTO reminder VALUES
('13:00', 'Sun', 1.5, 1, 1.5),
('17:00', 'Mon', 1.0, 0, NULL),
('17:30', 'Tue', 0.5, 0, NULL)
""")
con.commit()

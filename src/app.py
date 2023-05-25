import sqlite3
import ui
import db_interaction as db_int
import os.path
from os import path


if not path.exists("Stores/past.db"):
    open("Stores/past.db", 'x')
    db_int.init_past_db()


if not path.exists("Stores/reminders.db"):
    open("Stores/reminders.db", 'x')
    db_int.init_rem_db()

if not path.exists("Stores/UI.yaml"):
    open("Stores/UI.yaml", 'x')
    db_int.init_setting()

if not path.exists("Stores/WeeklyGoal.yaml"):
    open("Stores/WeeklyGoal.yaml", 'x')
    db_int.init_Weekly()


UI_frontend = ui.UI()
UI_frontend.place_ui()
UI_frontend.win_loop()
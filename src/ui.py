import tkinter as tk
class UI:
	def __init__(self):
		self.win = tk.Tk()
		self.reminder_in_frame = None
		self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 
		self.subjects = ['Science','Math','CS'];
#End indent
	def place_ui(self):
		#Input For The Reminder
		self.win.rowconfigure(0, weight=0,minsize=50)
		for i in range(3):
			self.win.columnconfigure(i, weight=0,minsize=50)
		self.reminder_in_frame = tk.Frame(self.win, bg='red')
		self.reminder_in_frame.grid(row=0, column=0)
		
		self.start_time = tk.Entry(master=self.reminder_in_frame,width=30)
		
		day_var = tk.StringVar(self.win)
		day_var.set(self.days[0])
		self.day_dropdown = tk.OptionMenu(self.reminder_in_frame, day_var, *self.days)
		
		self.duration = tk.Entry(master=self.reminder_in_frame, width=30)
		
		
		
		self.start_time.pack()
		self.day_dropdown.pack()
		self.duration.pack()
		
		#Subjects
		self.subject_frame = tk.Frame(self.win, bg='blue')
		self.subject_frame.grid(row=0, column=1) 
		self.add_subject = tk.Button(master=self.subject_frame, text="+")
		self.subject_list = tk.Frame(self.subject_frame, bg='red')
		self.subject_list.pack()
		self.subject_arr = []
		
		self.add_subject.pack()
		
		for i, e in enumerate(self.subjects):
			frame = tk.Frame(
					 master=self.subject_list,
					 borderwidth=1
					 )
			frame.grid(row=i)
			label = tk.Label(master=frame, text=e)
			label.pack()
		#end indent
		 
		#Set Settings
		self.setting_frame = tk.Frame(self.win, bg='green')
		self.setting_frame.grid(row=0, column=2)
		self.theme_frame = tk.Frame(self.setting_frame, bg='red')
		self.light_theme_button = tk.Button(self.theme_frame, text="light")
		self.dark_theme_button = tk.Button(self.theme_frame, text="dark")
		self.theme_frame.pack()
		self.light_theme_button.pack()
		self.dark_theme_button.pack()
		#Place Data
		
		#Place graph * 2
		
		#Set Reminders
		
       
	def win_loop(self):
		self.win.mainloop()
master = UI()
master.place_ui()
master.win_loop()

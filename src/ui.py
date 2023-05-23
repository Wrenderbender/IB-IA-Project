import tkinter as tk
class UI:
	def __init__(self):
		self.win = tk.Tk()
		self.reminder_in_frame = None
		self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 
		self.subjects = ['Science','Math','CS']
		#Stupid workaround because of Tkinter
		self.reminder_contents = []#this is stupid, ooh why can you just RETURN THE VALUE AN KEEP RUNNING? OR IDK MAYBE MAKE THAT A FUNCION??? JUST A THOUGHT
#End indent
	def get_val(self, area:str):#area gets the relevent frame, ie returns selected settings/subjects,etc
		if area == "reminder":
			return (self.start_time.get(), self.day_dropdown.get() ,self.duration.get())
		elif area == "subject":
			pass

	def place_ui(self):
		
		def _reminder_button_helper():#This is dumb and stupid but it must be done
			self.reminder_contents = [False,self.start_time.get(), day_var.get(), self.duration.get()]

		def _subject_button_helper():#AGAIN I HATET THIS >:(
			if self.subject_add_name.get() == '':
				return
			self.subjects.append(self.subject_add_name.get())
			print(self.subjects)
			for i, e in enumerate(self.subjects):
				frame = tk.Frame(
						master=self.subject_list,
						borderwidth=1
						)
				frame.grid(row=i)
				label = tk.Label(master=frame, text=e)
				label.pack()
			menu = self.subject_dropdown["menu"]
			menu.delete(0,"end")
			for string in self.subjects:
				menu.add_command(label=string, command=lambda val=string: sub_var.set(val))
			
		for i in range(3):
			self.win.rowconfigure(i, weight=1,minsize=50)
			self.win.columnconfigure(i, weight=1,minsize=50)
		#Input For The Reminder
		self.reminder_in_frame = tk.Frame(self.win, bg='red')
		self.reminder_in_frame.grid(row=0, column=0, sticky='WENS')
		
		self.start_time = tk.Entry(master=self.reminder_in_frame)
		
		day_var = tk.StringVar(self.win)
		day_var.set(self.days[0])
		day_var.trace_add('write', lambda *args: day_var.get())
		self.day_dropdown = tk.OptionMenu(self.reminder_in_frame, day_var, *self.days)
		sub_var = tk.StringVar(self.win)
		sub_var.set(self.subjects[0])
		sub_var.trace_add('write', lambda *args: sub_var.get())
		self.subject_dropdown = tk.OptionMenu(self.reminder_in_frame, sub_var, *self.subjects)	
		self.duration = tk.Entry(master=self.reminder_in_frame, width=30)
		
		self.add_rem = tk.Button(master=self.reminder_in_frame,text="+",command=_reminder_button_helper)

		self.start_time.pack()
		self.day_dropdown.pack()
		self.subject_dropdown.pack()
		self.duration.pack()
		self.add_rem.pack()

		#Subjects
		self.subject_frame = tk.Frame(self.win, bg='blue')
		self.subject_frame.grid(row=0, column=1, sticky="WENS") 
		self.add_subject = tk.Button(master=self.subject_frame, text="+", command=_subject_button_helper)
		self.subject_list = tk.Frame(self.subject_frame, bg='red')
		self.subject_list.pack()
		self.subject_arr = []
		
		self.add_subject.pack()
		self.subject_add_name = tk.Entry(self.subject_frame)
		self.subject_add_name.pack()

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
		self.setting_frame.grid(row=0, column=2, sticky="WENS")
		self.theme_frame = tk.Frame(self.setting_frame, bg='red')
		self.light_theme_button = tk.Button(self.theme_frame, text="light")
		self.dark_theme_button = tk.Button(self.theme_frame, text="dark")
		self.theme_frame.pack()
		self.light_theme_button.pack()
		self.dark_theme_button.pack()
		#Place Data
		self.data_frame = tk.Frame(self.win, bg="pink")
		self.today_frame = tk.Frame(self.data_frame, bg="orange")
		self.data_frame.grid(row=1, column=0, sticky="WENS")
		self.today_frame.pack()

		#Place graph * 2

		#Set Reminders
		

	def set_val(self, area:str):
		pass


	def win_loop(self):
		self.win.mainloop()
master = UI()
master.place_ui()
master.win_loop()
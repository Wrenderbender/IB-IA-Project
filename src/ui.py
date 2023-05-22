import tkinter as tk
class UI:
    def __init__(self):
        self.win = tk.Tk()
        self.reminder_in_frame = None
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 
        self.subjects = ['Science','Math','CS'];
    def place_ui(self):
       #Input For The Reminder
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


       for i, e in enumerate(self.subjects):
           frame = tk.Frame(
                   master=self.subject_list,
                   borderwidth=1
                   )
           frame.grid(row=i)
           label = tk.Label(master=frame, text=e)
           label.pack()

       self.add_subject.pack()
           
       #Set Settings

    

       #Place Data

       #Place graph * 2

       #Set Reminders

       
    def win_loop(self):
        self.win.mainloop()
master = UI()
master.place_ui()
master.win_loop()

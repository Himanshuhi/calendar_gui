import tkinter as tk
import calendar

class CalendarApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        
        self.calendar = tk.Text(self, width=30, height=10)
        self.calendar.pack()

        
        self.prev_button = tk.Button(self, text='Prev', command=self.prev_month)
        self.prev_button.pack(side='left')
        self.next_button = tk.Button(self, text='Next', command=self.next_month)
        self.next_button.pack(side='right')

        
        self.year = 2023
        self.month = 3
        self.display_month()

    def display_month(self):
        
        cal = calendar.month(self.year, self.month)

        
        self.calendar.delete('1.0', tk.END)
        self.calendar.insert(tk.END, cal)

    def prev_month(self):
      
        self.month -= 1
        if self.month == 0:
            self.month = 12
            self.year -= 1

       
        self.display_month()

    def next_month(self):
        
        self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1

        
        self.display_month()

root = tk.Tk()
app = CalendarApp(master=root)
app.mainloop()

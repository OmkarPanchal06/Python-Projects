import tkinter as tk
from time import strftime

def update_time():
    time_string = strftime('%H:%M:%S %p')
    date_string = strftime('%A, %d %B %Y')
    
    label_time.config(text=time_string)
    label_date.config(text=date_string)
    
    label_time.after(1000, update_time)

#main_window
root = tk.Tk()
root.title('Digital Clock')
root.geometry('500x200')
root.configure(bg='#0a0a0a') 

#Time_label
label_time = tk.Label(
    root,
    font=('Helvetica Neue', 40, 'bold'),
    background='#0a0a0a',
    foreground='#00FFCC'  
)
label_time.pack(pady=20)

#Date_label
label_date = tk.Label(
    root,
    font=('Helvetica Neue', 30),
    background='#0a0a0a',
    foreground='#00FFCC'
)
label_date.pack(pady=10)

update_time()

root.mainloop()

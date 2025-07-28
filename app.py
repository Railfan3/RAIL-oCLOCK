import tkinter as tk
from tkinter import messagebox, ttk
import os
import json
import sys

# Helper to find resource paths (works inside .exe too)
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller's temp folder
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Paths
DATA_FOLDER = resource_path("data")
STATION_MAP_FILE = os.path.join(DATA_FOLDER, "stations.json")

# Load station name-to-code mapping
station_map = {}
try:
    with open(STATION_MAP_FILE, 'r') as f:
        station_map = json.load(f)
except Exception:
    messagebox.showerror("Error", "stations.json mapping file not found in data folder.")
    sys.exit(1)

# Fetch timetable function
def fetch_timetable():
    user_input = entry_station.get().strip().upper()
    station_code = station_map.get(user_input, user_input)

    file_path = os.path.join(DATA_FOLDER, f"{station_code}.json")

    for row in tree.get_children():
        tree.delete(row)

    if not os.path.exists(file_path):
        messagebox.showerror("Error", f"No timetable data found for station: {user_input}")
        return

    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            trains = data.get('trains', [])

            if not trains:
                messagebox.showinfo("Info", "No trains found in data.")
                return

            for train in trains:
                tree.insert('', 'end', values=(
                    train.get('trainNo', 'N/A'),
                    train.get('trainName', 'N/A'),
                    train.get('arrival', 'N/A'),
                    train.get('departure', 'N/A'),
                    train.get('runDays', 'N/A')
                ))
    except Exception as e:
        messagebox.showerror("Error", f"Error loading data: {str(e)}")

# GUI Setup
root = tk.Tk()
root.title("RAIL'oCLOCK - Track departures and arrivals.")
root.state('zoomed')
root.configure(bg='#f0f4f7')

# Style
style = ttk.Style()
style.theme_use('clam')
style.configure("Treeview",
                background="#ffffff",
                foreground="black",
                rowheight=30,
                fieldbackground="#ffffff",
                font=('Segoe UI', 12))
style.configure("Treeview.Heading",
                font=('Segoe UI', 14, 'bold'),
                background="#2e3f4f",
                foreground="white")
style.map('Treeview', background=[('selected', '#d1eaff')])

# Header
tk.Label(root,
         text="🚆 RAIL'oCLOCK - Never Miss a Train Again !",
         font=('Segoe UI', 28, 'bold'),
         bg='#f0f4f7',
         fg='#2e3f4f').pack(pady=30)

# Input Frame
input_frame = tk.Frame(root, bg='#f0f4f7')
input_frame.pack(pady=10)

tk.Label(input_frame,
         text="Enter Station Name or Code:",
         font=('Segoe UI', 14),
         bg='#f0f4f7').pack(side='left', padx=10)

entry_station = tk.Entry(input_frame,
                         width=30,
                         font=('Segoe UI', 14),
                         justify='center',
                         bg='#ffffff',
                         fg='#2e3f4f',
                         relief='solid',
                         bd=1)
entry_station.pack(side='left', padx=10)

tk.Button(root,
          text="Get Timetable",
          font=('Segoe UI', 14, 'bold'),
          bg='#2e3f4f',
          fg='white',
          activebackground='#3e5064',
          activeforeground='white',
          relief='flat',
          padx=15,
          pady=5,
          command=fetch_timetable).pack(pady=20)

# Treeview Frame
tree_frame = tk.Frame(root, bg='#f0f4f7')
tree_frame.pack(fill='both', expand=True, padx=30, pady=10)

scroll_y = ttk.Scrollbar(tree_frame, orient='vertical')
scroll_x = ttk.Scrollbar(tree_frame, orient='horizontal')

columns = ('Train No', 'Train Name', 'Arrival', 'Departure', 'RunDays')
tree = ttk.Treeview(tree_frame,
                    columns=columns,
                    show='headings',
                    yscrollcommand=scroll_y.set,
                    xscrollcommand=scroll_x.set)

scroll_y.config(command=tree.yview)
scroll_x.config(command=tree.xview)
scroll_y.pack(side='right', fill='y')
scroll_x.pack(side='bottom', fill='x')

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor='center', width=200)

tree.pack(fill='both', expand=True)

root.mainloop()

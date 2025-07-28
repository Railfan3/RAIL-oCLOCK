🚆 RAIL'oCLOCK
RAIL'oCLOCK is a lightweight offline desktop application that displays Indian railway timetables, platform numbers, and source-to-destination train routes. It is designed to work without any internet connection using preloaded JSON data, making it fast and efficient.

⚠️ Note: This application supports a limited number of specific stations only, as real-time government APIs are not accessible. Data is manually compiled and stored in local JSON files.

🧠 Features
🔍 Station Lookup: Enter a station name or code to view trains stopping at that station.

🗓️ Detailed Timetables: Arrival and departure timings along with platform numbers.

🛤️ Complete Routes: Displays all intermediate stations between the source and destination.

📁 Offline Functionality: Works entirely offline with local JSON data.

🖥️ Simple GUI: Built with Python's Tkinter for a clean and responsive user experience.

🛠️ Windows Executable: Ready-to-use .exe file – no setup required.

📌 Important Notes
This app only supports selected stations included in the stations.json file.

Due to the unavailability of public Indian Railways APIs, the app cannot fetch or update real-time data.

You can expand the app by adding more station or train timetable JSON files in the data/ directory.

🗂️ Project Structure
bash
Copy
Edit
railway_tt/
│
├── app.py                # Main GUI logic
├── rr.py / rr2.py        # Backend functions for data parsing and filtering
├── app.spec              # PyInstaller configuration
├── app_icon.ico          # Application icon
├── dist/                 # Executable output folder
└── data/
    ├── stations.json     # List of supported stations
    ├── [train_data].json # Timetables of specific trains
🛠️ Tech Stack
Language: Python 3.x

GUI: Tkinter

Data: JSON

Packaging: PyInstaller

🚀 How to Run
💻 Run from Source
bash
Copy
Edit
git clone https://github.com/yourusername/railoclock.git
cd railoclock
python app.py
Ensure data/ folder is present in the same directory.

🪟 Run Executable
Navigate to the dist/ folder and double-click:

Copy
Edit
dist/
└── app.exe
No Python installation needed.

📸 Screenshots
(Insert GUI screenshots here)

🔮 Future Plans
Live API integration (if access becomes available)

Real-time train status

Multi-station bulk search

Cross-platform (Linux/Mac) version

👨‍💻 Developed By
Mukul Chouhan
🎓 Electronics and Communication Engineering
🌐 [https://www.linkedin.com/in/mukul-chouhan-596291295/] 

📄 License
This project is licensed under the MIT License.
See the LICENSE file for more information.





import requests
import json
import os

# URL of train schedules dataset from Datameet
url = "https://raw.githubusercontent.com/datameet/railways/master/schedules.json"

print("📥 Downloading the Indian Railways schedule data...")

try:
    response = requests.get(url)
    response.raise_for_status()
    all_schedules = response.json()
except Exception as e:
    print("❌ Failed to download or parse JSON:", e)
    exit(1)

# Extract all unique station codes
station_codes = sorted({s.get("station_code") for s in all_schedules if s.get("station_code")})

# Helper function to format days
def format_days(days_set):
    DAY_CH = "SMTWTFS"
    return " ".join(DAY_CH[d - 1] for d in sorted(days_set))

# Create output directory
os.makedirs("timetables", exist_ok=True)

# Loop over each station
for station_code in station_codes:
    station_schedules = [s for s in all_schedules if s.get("station_code") == station_code]

    if not station_schedules:
        continue

    trains = {}
    for s in station_schedules:
        tno = s.get("train_number")
        if not tno:
            continue

        if tno not in trains:
            trains[tno] = {
                "trainNo": tno,
                "trainName": s.get("train_name", "Unknown"),
                "arrival": "-",
                "departure": "-",
                "days": set()
            }

        if s.get("arrival") and s["arrival"].lower() != "none":
            trains[tno]["arrival"] = s["arrival"][:5]

        if s.get("departure") and s["departure"].lower() != "none":
            trains[tno]["departure"] = s["departure"][:5]

        day = s.get("day")
        if isinstance(day, int) and 1 <= day <= 7:
            trains[tno]["days"].add(day)

    output = {
        "station": {
            "code": station_code,
            "name": station_schedules[0].get("station_name", "Unknown")
        },
        "trains": []
    }

    for t in trains.values():
        output["trains"].append({
            "trainNo": t["trainNo"],
            "trainName": t["trainName"],
            "arrival": t["arrival"],
            "departure": t["departure"],
            "runDays": format_days(t["days"])
        })

    filename = f"timetables/{station_code}_timetable.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"✅ Saved {len(output['trains'])} trains to '{filename}'")

print("\n🎉 All timetables generated successfully!")

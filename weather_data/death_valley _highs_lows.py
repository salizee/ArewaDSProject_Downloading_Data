#Error Checking
from pathlib import Path
import csv
from datetime import datetime
path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
for index, column_header in enumerate(header_row):
 print(index, column_header)

 path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

# Extract dates, and high and low temperatures.
dates, highs, lows = [], [], []
for row in reader:
 current_date = datetime.strptime(row[2], '%Y-%m-%d')
 high = int(row[3])
 low = int(row[4])
 dates.append(current_date)

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

# Extract dates, and high and low temperatures.
dates, highs, lows = [], [], []
for row in reader:
 current_date = datetime.strptime(row[2], '%Y-%m-%d')
 high = int(row[3])
 low = int(row[4])
 dates.append(current_date)

 for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
import matplotlib.pyplot as plt

# Plot the high and low temperatures.
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
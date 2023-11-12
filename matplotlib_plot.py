import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import os

# Function to select files
def select_files():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_paths = filedialog.askopenfilenames(filetypes=[("CSV files", "*.csv")])
    return list(file_paths)

# Read selected files
file_paths = select_files()
data_frames = [pd.read_csv(file) for file in file_paths]

# Create a new figure and axis
fig, ax = plt.subplots()

# Plot data from each file
colors = ['blue', 'black', 'red', 'green', 'purple', 'orange']  # Extend this list as needed
for i, (file_path, data) in enumerate(zip(file_paths, data_frames)):
    color = colors[i % len(colors)]  # Cycle through colors
    label = os.path.basename(file_path)  # Use file name as label
    ax.plot(data['E/V'], data['I/uA'], color=color, label=label)

# Set the black border and increase the thickness
border_width = 2
ax.spines['bottom'].set_color('black')
ax.spines['bottom'].set_linewidth(border_width)
ax.spines['top']. set_color('black')
ax.spines['top'].set_linewidth(border_width)
ax.spines['left'].set_color('black')
ax.spines['left'].set_linewidth(border_width)
ax.spines['right'].set_color('black')
ax.spines['right'].set_linewidth(border_width)

# Set smaller tickers with increased fontsize
tick_length = 4
tick_width = 1
tick_label_fontsize = 10  # Adjust the fontsize as needed
ax.tick_params(axis='both', which='both', length=tick_length, width=tick_width, labelsize=tick_label_fontsize)
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())

# Set labels and title
ax.set_xlabel('Potential (V)', fontsize=14, fontname='Times New Roman')
ax.set_ylabel('Current (\u03BCA)', fontsize=14, fontname='Times New Roman')
ax.legend()

'''
# Save the plot as a high-resolution JPEG
plt.savefig('../Ru_I_Time', dpi=500)
'''

# Show the plot
plt.show()

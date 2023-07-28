import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import AutoMinorLocator

# Load the data from CSV file
data = pd.read_csv('../data/20230220_Cd_UPD_02_00.csv')

data_2 = pd.read_csv('../data/20230120_Cd_UPD_02_-02.csv')
data_3 = pd.read_csv('../data/20230120_Cd_UPD_02_-04.csv')
data_4 = pd.read_csv('../data/20230120_Cd_UPD_02_-06.csv')
data_5 = pd.read_csv('../data/20230120_Cd_UPD_02_-08.csv')
data_6 = pd.read_csv('../data/20230120_Cd_UPD_02_-1.csv')
data_7 = pd.read_csv('../data/20230120_S_UPD_00.csv')


# Create a new figure and axis
fig, ax = plt.subplots()

# Plot your data
ax.plot(data['E/V'], data['I/uA'], color='black')

ax.plot(data_2['E/V'], data_2['I/uA'], color='orange')

ax.plot(data_3['E/V'], data_3['I/uA'], color='purple')
ax.plot(data_4['E/V'], data_4['I/uA'], color='blue')
ax.plot(data_5['E/V'], data_5['I/uA'], color='green')
ax.plot(data_6['E/V'], data_6['I/uA'], color='red')
'''
ax.plot(data_7['E/V'], data_7['I/uA'], color='black')
'''

# Set the black border and increase the thickness
border_width = 2
ax.spines['bottom'].set_color('black')
ax.spines['bottom'].set_linewidth(border_width)
ax.spines['top'].set_color('black')
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
ax.set_xlabel('Potential (V vs. Ag/AgCl)', fontsize=14, fontname='Times New Roman')
ax.set_ylabel('Current density (\u03BCA cm\u00b2)', fontsize=14, fontname='Times New Roman')

# Save the plot as a high-resolution JPEG
plt.savefig('Cd_CV_Au_2.jpg', dpi=1500)
# Show the plot
plt.show()


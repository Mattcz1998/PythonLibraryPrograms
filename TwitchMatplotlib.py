# ----- Matplotlib program that graphs the Top 50 streamers and their average ad revenue -----
from matplotlib import pyplot as plt
from matplotlib import style

import numpy as np
import pandas as pd

style.use('ggplot')

# Reading CSV file
data = pd.read_csv('twitchdata-adrevenue.csv')
df = pd.DataFrame(data)

# Calculate avg ad revenue
a = df['Views_gained']/1000
a2 = a * 5

# Creating horizontal bar chart
fig = plt.figure(figsize=(500,10))
plt.barh(df['Channel'],a2)

# Titles and labels
plt.title('Top 50 Twitch Streamers Avg Ad Revenue Chart')
plt.ylabel('Channel Name')
plt.xlabel('Ad revenue ($)')
plt.tick_params(axis = 'y', which='major', labelsize=7.5)

# To create bar labels
for index, value in enumerate(a2):
    plt.text(value, index, str('${0:,.0f}'.format(np.around(value))), font={'size': 6})

# Change step parameter to adjust the X Tick Frequency
x = np.trim_zeros(np.arange(min(np.around(list(a2))), max(np.around(list(a2))), step=200_000), 'f')
plt.xticks(x, ['${0:,.0f}'.format(v,i) for i,v in enumerate(x)],rotation=20)

plt.show()
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time

# Array with 7 rows for 7 days of a week and 24 columns for 24 hours of a day
data = np.zeros([7, 24])

# List of hours
hours = []
for hour in range(24):
    hours.append(hour)

# Iterate through subreddits and extract all timestamps
subreddits = ['mentalhealth', 'depression', 'suicidewatch']

for subreddit in subreddits:
    subreddit_data = pd.read_csv(f'time_stamp_data/{subreddit}_timestamps.csv')
    total_posts = len(subreddit_data)

    for row in range(total_posts):
        epoch = int(subreddit_data[f"{subreddit}_timestamps"].iloc[row])
        day_posted = time.gmtime(epoch).tm_wday
        hour_posted = time.gmtime(epoch).tm_hour

        if hour_posted >= 5:
            hour_posted -= 5  # Converting GMT to EST and storing

        else:
            hour_posted = 24 + (hour_posted - 5)  # Converting GMT to EST and storing

        # Count number of posts and add to the big array
        if hour_posted < 5:
            if day_posted > 0:
                data[day_posted-1][hour_posted] += 1
            else:
                data[6][hour_posted] += 1

        else:
            data[day_posted][hour_posted] += 1

        data[day_posted][hour_posted] += 1

# Set up graph styling
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
linestyle = ['-', '-', '--', '--', '-.', '-.', ':']
color = ['r', 'k', 'r', 'k', 'r', 'k', 'r']

for day in range(7):
    plt.plot(hours, data[day], label=days[day], linestyle=linestyle[day], color=color[day])

plt.xlabel("Hour of the day (EST)")
plt.ylabel("Number of posts")
plt.xticks(np.arange(24))
plt.legend(title='Days of the week')
plt.grid()
plt.title('Number of posts posted at X hour on Y day of the week', size=20)
plt.show()
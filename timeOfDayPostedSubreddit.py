import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time


data = np.zeros([3, 25])  # 3 rows for three subreddits and 24 columns for 24 hours of the day plus 1 additional to complete the loop

subreddits = ['mentalhealth', 'depression', 'suicidewatch']

# Iterate through each csv file to add number of posts in each day
post_count = 0
n = 0
for subreddit in subreddits:

    subreddit_data = pd.read_csv(f'time_stamp_data/{subreddit}_timestamps.csv')

    total_posts = len(subreddit_data)

    for row in range(total_posts):
        post_count += 1
        epoch = int(subreddit_data[f"{subreddit}_timestamps"].iloc[row])
        hour_posted = time.gmtime(epoch).tm_hour

        if hour_posted >= 5:
            data[n][hour_posted - 5] += 1  # Converting GMT to EST and storing

        else:
            data[n][24 + (hour_posted - 5)] += 1  # Converting GMT to EST and storing

    n += 1

print(post_count)

hours = []
for hour in range(24):
    hours.append(hour)

angles = np.linspace(0, 2*np.pi, len(hours), endpoint=False)  # Finding all values of angles required

# Assigning last value equal to first value to complete the loop
for row in range(3):
    data[row][24] = data[row][0]

angles = np.append(angles, angles[0])
hours.append(hours[0])

# Reverse the values to read clockwise
data = np.flip(data, axis=1)
hours.reverse()

fig = plt.figure(figsize=(8, 8))
ax = plt.subplot(polar=True)

ax.plot(angles, data[1], 'r-', linewidth=2, label='r/depression')
ax.fill(angles, data[1], alpha=0.25, color='red')

ax.plot(angles, data[2], 'y-', linewidth=2, label='r/suicidewatch')
ax.fill(angles, data[2], alpha=0.20, color='yellow')

ax.plot(angles, data[0], 'b-', linewidth=2, label='r/mentalhealth')
ax.fill(angles, data[0], alpha=0.15, color='blue')

ax.set_thetagrids(angles * 180/np.pi, hours, size=12)
ax.set_rticks([5000, 10000, 15000, 20000])
ax.set_rlabel_position(30)
ax.set_theta_offset(90 * np.pi / 180)

plt.title('Number of posts posted at X hour of the day in EST', size=20)
plt.legend(title='Subreddits', bbox_to_anchor=(1.4, 1))
plt.show()

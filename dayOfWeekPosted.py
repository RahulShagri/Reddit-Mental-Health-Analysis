import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time


data = np.zeros([3, 7])  # 3 rows for three subreddits and 7 columns for 7 days of the week plus 1 to complete the loop

subreddits = ['mentalhealth', 'depression', 'suicidewatch']

# Iterate through each csv file to add number of posts in each day

n = 0

for subreddit in subreddits:
    subreddit_data = pd.read_csv(f'time_stamp_data/{subreddit}_timestamps.csv')

    total_posts = len(subreddit_data)

    for row in range(total_posts):
        epoch = int(subreddit_data[f"{subreddit}_timestamps"].iloc[row])
        hour_posted = time.gmtime(epoch).tm_hour
        day_posted = time.gmtime(epoch).tm_wday

        if hour_posted < 5:
            if day_posted > 0:
                data[n][day_posted-1] += 1
            else:
                data[n][6] += 1

        else:
            data[n][day_posted] += 1

    n += 1

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
X_axis = np.arange(7)

plt.bar(X_axis, data[1], width=0.3, label='r/depression', color='r')
plt.bar(X_axis + 0.3, data[2], width=0.3, label='r/suicidewatch', color='y')
plt.bar(X_axis + 0.6, data[0], width=0.3, label='r/mentalhealth', color='b')
plt.xticks(X_axis + 0.3, days)
plt.xlabel("Days of the week")
plt.ylabel("Number of posts")

plt.title('Number of posts posted on X day of the week', size=20)
plt.legend(title='Subreddits', bbox_to_anchor=(1.2, 1))
plt.show()


# angles = np.linspace(0, 2 * np.pi, len(days), endpoint=False)  # Finding all values of angles required
#
# # Assigning last value equal to first value to complete the loop
# for row in range(3):
#     data[row][7] = data[row][0]
# angles = np.append(angles, angles[0])
# days.append(days[0])
#
# # Reverse the values to read clockwise
# data = np.flip(data, axis=1)
# days.reverse()
#
# fig = plt.figure(figsize=(8, 8))
# ax = plt.subplot(polar=True)
#
# ax.plot(angles, data[1], 'ro-', linewidth=2, label='r/depression')
# ax.fill(angles, data[1], alpha=0.25, color='red')
#
# ax.plot(angles, data[2], 'yo-', linewidth=2, label='r/suicidewatch')
# ax.fill(angles, data[2], alpha=0.2, color='yellow')
#
# ax.plot(angles, data[0], 'bo-', linewidth=2, label='r/mentalhealth')
# ax.fill(angles, data[0], alpha=0.15, color='blue')
#
# ax.set_thetagrids(angles * 180 / np.pi, days, size=12)
# ax.tick_params(axis='x', which='major', pad=25)
# ax.set_rticks([10000, 30000, 50000])
# ax.set_rlabel_position(0)
# ax.set_theta_offset(90 * np.pi / 180)
#
# plt.title('Number of posts posted on X day of the week', size=20)
# plt.legend(title='Subreddits', bbox_to_anchor=(1.5, 1))
# plt.show()

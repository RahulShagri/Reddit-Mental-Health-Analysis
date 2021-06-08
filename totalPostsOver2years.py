import matplotlib.dates
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time
from time import mktime
from datetime import datetime

data = np.empty((0,714))

subreddits = ['depression']

for subreddit in subreddits:
    subreddit_data = pd.read_csv(f'time_stamp_data/{subreddit}_timestamps.csv')
    total_posts = len(subreddit_data)

    previous_date = time.gmtime(int(subreddit_data[f"{subreddit}_timestamps"].iloc[0]))
    previous_date = datetime.fromtimestamp(mktime(previous_date)).date()

    number_of_posts_in_day = 0

    number_of_posts = []
    dates = []

    for row in range(total_posts):
        epoch = int(subreddit_data[f"{subreddit}_timestamps"].iloc[row])
        day_posted = time.gmtime(epoch)
        dt = datetime.fromtimestamp(mktime(day_posted))

        if dt.date() == previous_date:
            number_of_posts_in_day += 1
        else:
            number_of_posts.append(number_of_posts_in_day)
            dates.append(previous_date)
            number_of_posts_in_day = 1
            previous_date = dt.date()

    number_of_posts.append(number_of_posts_in_day)
    dates.append(previous_date)

    data = np.append(data, np.array([number_of_posts]), axis=0)
    data = np.append(data, np.array([dates]), axis=0)

for row in range(0, 2, 2):
    dates = matplotlib.dates.date2num(data[row+1])
    plt.plot(dates, data[row])

plt.show()
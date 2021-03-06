import calendar
import praw
import time
import csv

from psaw import PushshiftAPI

# recording the time the program started
program_start_time = time.time()
print(f"Program started at {program_start_time}")

# connecting to the Reddit API
reddit = praw.Reddit(
    client_id='pPvxC5J_IXod_Q',
    client_secret='V-xfZNlxktrOMaXs2fXqOIecmUkL3w',
    user_agent='time-stamp-extractor'
)

api = PushshiftAPI(reddit)

# Collecting timestamps of posts made between start and end time (total 2 years)
start_time = 'Jun 1, 2019 @ 00:00:00 UTC'
end_time = 'May 31, 2021 @ 23:59:61 UTC'

start_time = calendar.timegm(time.strptime(start_time, '%b %d, %Y @ %H:%M:%S UTC'))
end_time = calendar.timegm(time.strptime(end_time, '%b %d, %Y @ %H:%M:%S UTC'))

# Extracting subreddit_data from three subreddits
subreddits = ['mentalhealth', 'depression', 'suicidewatch']

for subreddit in subreddits:
    print(f"\nCollecting r/{subreddit} data...")
    submissions = list(api.search_submissions(after=start_time,
                                              before=end_time,
                                              filter=['created_utc'],
                                              subreddit=subreddit))

    # Writing subreddit_data to a CSV file after collection
    with open(f'time_stamp_data/{subreddit}_timestamps.csv', mode='w', encoding='utf-8') as timestamps_file:
        timestamps_writer = csv.writer(timestamps_file, delimiter=',')
        timestamps_writer.writerow([f'{subreddit}_timestamps'])

        for submission in submissions:
            timestamps_writer.writerow([submission.created_utc])

    print(f"Completed collecting r/{subreddit} data.")

# Recording program stop time
program_stop_time = time.time()
print(f"\nProgram ended at {program_stop_time}")

total_time = program_stop_time - program_start_time

hours = int(total_time / 3600)
minutes = int((total_time / 60) % 60)
seconds = int(total_time - int(hours) * 3600 - minutes * 60)

# Program took the following amount of time run
print(f"Total time taken: {hours}h {minutes}m {seconds}s")

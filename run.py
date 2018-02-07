import config
import praw

reddit = praw.Reddit(client_id= config.client_id,
                     client_secret= config.client_secret,
                     user_agent= config.user_agent)

for submission in reddit.subreddit('learnpython').hot(limit=10):
    print(submission.title)
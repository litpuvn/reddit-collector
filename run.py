import config
import praw

reddit = praw.Reddit(client_id= config.client_id,
                     client_secret= config.client_secret,
                     user_agent= config.user_agent)

for comment in reddit.subreddit('opiatesrecovery').comments(limit=50):
    print(comment.body.encode('utf-8'))
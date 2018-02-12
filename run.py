import config
import praw

reddit = praw.Reddit(client_id= config.client_id,
                     client_secret= config.client_secret,
                     user_agent= config.user_agent)

subreddit = reddit.subreddit('Catan')

submissions = subreddit.new(limit="None")

print(subreddit)
print('_______________________________________________________')
for submission in submissions:
    submission.comments.replace_more(limit=None)
    print(submission.title)
    for comment in submission.comments.list():
        print("\t" + comment.body)
print('_______________________________________________________')

if __name__ == '__main__':
    print("Collecting...")
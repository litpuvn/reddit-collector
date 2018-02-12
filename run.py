import config
import praw
import json
import argparse


reddit = praw.Reddit(client_id= config.client_id,
                     client_secret= config.client_secret,
                     user_agent= config.user_agent)

def get_parser():
    parser = argparse.ArgumentParser(description="Reddit Downloader")
    parser.add_argument("-s",
                        "--subreddit",
                        dest="subreddit",
                        help="Subreddit to PRAW",
                        default='all')

    return parser

def prawSubreddit(subName):
    print("Collecting from /r/{}...".format(subName))
    submissionCount = 0
    commentCount = 0
    fileCount = 0
    redditData = {}

    subreddit = reddit.subreddit(subName)
    submissions = subreddit.new(limit=None)
    redditData[str(subreddit)] = [{}]

    # Iterate through each submissions and following comments
    for submission in submissions:
        submissionCount += 1
        submission.comments.replace_more(limit=None)
        redditData[str(subreddit)][0][submission.fullname] = [{}]
        redditData[str(subreddit)][0][submission.fullname][0]['0_title'] = submission.title
        redditData[str(subreddit)][0][submission.fullname][0]['1_text'] = submission.selftext
        redditData[str(subreddit)][0][submission.fullname][0]['comments'] = [{}]

        for comment in submission.comments.list():
            commentCount += 1
            redditData[str(subreddit)][0][submission.fullname][0]['comments'][0][comment.fullname] = comment.body

        updateTerminal(submissionCount, commentCount, )

        if(submissionCount % 300 == 0):
            writeOutput("{}_{}.txt".format(subName,fileCount),redditData)
            fileCount += 1
            redditData = {}
            subreddit = reddit.subreddit(subName)
            redditData[str(subreddit)] = [{}]

    print("Finished Collecting.")
    writeOutput("{}_{}.txt".format(subName,fileCount),redditData)


def writeOutput(fileName, data):
    outputFile = open(fileName, "w")
    outputFile.write(json.dumps(data, sort_keys=True))

# After X amount of seconds, update progress to terminal
def updateTerminal( subCount, comCount):
    if ((subCount % 350) == 0):
        print("Downloaded: {} Submissions".format(subCount))
        print("Downloaded: {} Comments".format(comCount))

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

if __name__ == '__main__':

    parser = get_parser()
    args = parser.parse_args()

    prawSubreddit(args.subreddit)
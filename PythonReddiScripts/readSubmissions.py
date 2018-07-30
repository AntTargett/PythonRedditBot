import praw
print("Running Python Scipt")

print("Creating Praw using reddit bot 1 from praw")
reddit = praw.Reddit('bot1')

print("Successful")

subreddit = reddit.subreddit("programming")

print("Successfully accessed subreddit 'r/programming")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")
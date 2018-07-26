import praw
import pdb
import re
import os

print("Running Python Scipt")

print("Creating Praw using reddit bot 1 from praw")
reddit = praw.Reddit('bot1')

print("Successful")

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
       posts_replied_to = f.read()
       posts_replied_to = posts_replied_to.split("\n")
       posts_replied_to = list(filter(None, posts_replied_to))

    
subreddit = reddit.subreddit("pythonforengineers")

print("Successfully accessed subreddit 'r/pythonforengineers")




for submission in subreddit.new(limit=3):
    if submission.id not in posts_replied_to:
        if re.search("i love python", submission.title, re.IGNORECASE):
            submission.reply("ImAnAnt bot says:  iz okay")
            print("Bot replying to : ", submission.title)
            posts_replied_to.append(submission.id)

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
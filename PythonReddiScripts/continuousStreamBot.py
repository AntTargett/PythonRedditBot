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




for comment in subreddit.stream.comments():
    if re.search("ImAnAnt Help", comment.body, re.IGNORECASE):
        ImAnAnt_reply = "ImAnAntBot: " + "halp me I am in pain"
        comment.reply(ImAnAnt_reply)
        print(str(comment) + ImAnAnt_reply)
for post_id in posts_replied_to:
    f.write(post_id + "\n")
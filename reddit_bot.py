
#!/usr/bin/python
import time
import praw
import pdb
import re
import os

reddit = praw.Reddit('bot1')
# loop to keep running
while True:
  if not os.path.isfile("posts_notified.txt"):
    posts_notified = []

  else:
    with open("posts_notified.txt", "r") as f:
      posts_notified = f.read()
      posts_notified = posts_notified.split("\n")
      posts_notified = list(filter(None, posts_notified))

    subreddit = reddit.subreddit("beachparty")

  for submission in subreddit.new(limit=5):
    message = 'Hi there, ' + submission.author.name + ' has made a new post in BP, ' +"[" + submission.title + "](" + submission.permalink + "). To shut me up click the block user button below. Have a great day!"
    if submission.id not in posts_notified:
      with open("approved_submitters.txt", "r") as f:
        usernames = f.read()
        usernames = usernames.split("\n")
        usernames = list(filter(None, usernames))
        with open("removed_names.txt", "r") as r:
          removed_users = r.read()
          removed_users = removed_users.split("\n")
          removed_users = list(filter(None, removed_users))
          print usernames
          print removed_users
          for username in usernames:
            print username
            if username not in removed_users:
              print username
              reddit.redditor(username).message('New Post in BeachParty!', message)

      print("Bot notifying users of : ", submission.author, "'s post", submission.title)

      posts_notified.append(submission.id)

  with open("posts_notified.txt", "w") as f:
    for post_id in posts_notified:
      f.write(post_id + "\n")

  time.sleep(100.0)

import praw
import random
import datetime
import time
from praw.reddit import Comment
from textblob import TextBlob
'''
#connect to Reddit
reddit = praw.Reddit('anotha_bot1')
subreddit = reddit.subreddit('BotTown2')
list_subreddit = list(subreddit.hot(limit=None))


submission_upvotes = 0
submission_downvotes = 0
comment_upvotes = 0
comment_downvotes = 0

for submission in list_subreddit:
    submission.comments.replace_more(limit=None)
    blob = TextBlob(str(Comment.body))
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    blob = TextBlob(str(Comment.body))

#upvote submissions
    if 'trump' in submission.title.lower():
        submission.upvote()
        submission_upvotes +=1
        print('Submission Upvoted!')  
#downvote submissions  
    if 'biden' in submission.title.lower():
        submission.downvote()
        submission_upvotes +=1
        print('Submission Downvoted!')
    if 'harris' in submission.title.lower():
        submission.downvote()
        submission_upvotes +=1
        print('Submission Downvoted!')
    

# Downvote and upvote comments for opposition using TextBlob 
for comment in submission.comments.list():
    blob = TextBlob(str(Comment.body))
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if 'Trump' in comment.body.lower() and polarity > 0.5:
        comment.upvote()
        comment_upvotes +=1
        print('comment upvoted!')
    if 'Harris' in comment.body.lower() and polarity > 0.5:
        comment.downvote()
        comment_downvotes +=1
        print('comment downvoted!')
    if 'Trump' in comment.body.lower() and subjectivity > 0:
        comment.upvote()
        comment_upvotes +=1
        print('comment upvoted!')
    if 'Harris' in comment.body.lower() and subjectivity > 0:
        comment.downvote()
        comment_downvotes +=1
        print('comment downvoted!')
'''

''''
print('Submission_upvotes=',submission_upvotes)
print('Submission_downvotes=', submission_downvotes)
print('Comment_upvotes=',comment_upvotes)
print('Comment_downvotes=', comment_downvotes)

time.sleep(6)
'''

print('Submission_upvotes=')
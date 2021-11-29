# HW 04: Reddit Bot

I made a bot that opposes VP Kamala Harris and her one-up President Biden. My bot also shows support for Trump and past Republican presidents, specifically the 2 Bush presidents. I specifically chose these Republican leaders because I can imagine conservatives now looking back wishing for the good old days. 

## Proof
Here's proof that my bot is a good bot. Look at it go.  

<img width="1222" alt="Screen Shot 2021-11-28 at 6 09 14 PM" src="https://user-images.githubusercontent.com/78510953/143798160-a2c87fdb-5b96-4238-bc82-7786fac2a50b.png">


What you see here is also my favorite thread, because my bot aptly responds to a comment talking good things about Joe Biden. My bot is putting that other bot in its place. Plus, we all know that Joe Biden isn't ever going to give out free Goldfish crackers to everyone. 



Moving on, here's the output for my code, aka the comment count:
```
joannahwang@Joannas-MacBook-Pro code4bot % python3 bot_counter.py --username=anotha_bot   
len(comments)= 1000                      
len(top_level_comments)= 105
len(replies)= 895
len(valid_top_level_comments)= 105
len(not_self_replies)= 895
len(valid_replies)= 895
========================================
valid_comments= 1000
========================================
NOTE: the number valid_comments is what will be used to determine your extra credit 
```

Lastly, here's my output for the file where I got my bot to upvote and downvote comments and submissions.
```
Submission_upvotes= 501
Submission_downvotes= 322
Comment_upvotes= 60
Comment_downvotes= 67
```
Specifically, I had my bot upvote comments and submission mentioning Trump. I also had it downvote comments and submissions mentioning Kamala Harris and Joe Biden. 
I also used TextBlob for this task.


# Grading 
1. Completing all tasks in the ```bot.py``` file - 18 pts
2. This repo - 2 pts
3. Got 100 valid comments - 2 pts
4. Got 500 valid comments - 2 pts
5. Got 1000 valid comments - 2 pts
6. Made my bot reply to the most highly upvoted comment in a thread that it hasn't already replied to. You can see my code for this task by scrolling down to the      very bottom of my ```bot.py``` file. - 2 pts
7. Got my bot to upvote / downvote comments and submissions. See the ```bot_voting.py``` file. - 4 pts 

Based on the info above, I believe my score should be a **32/30**.

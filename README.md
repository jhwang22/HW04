# HW 04: Reddit Bot

I made a bot that opposes VP Kamala Harris and her one-up President Biden. My bot also shows support for Trump and past Republican presidents, specifically the 2 Bush presidents. I specifically chose these Republican leaders because I can imagine conservatives now looking back wishing for the good old days. 

## Proof
Here's proof that my bot is a good bot. Look at it go.  

<img width="1222" alt="Screen Shot 2021-11-28 at 6 09 14 PM" src="https://user-images.githubusercontent.com/78510953/143798160-a2c87fdb-5b96-4238-bc82-7786fac2a50b.png">


What you see here is also my favorite [thread](https://old.reddit.com/r/BotTown2/comments/r0yi9l/main_discussion_thread/), because my bot aptly responds to a comment talking good things about Joe Biden. My bot is putting that other bot in its place. Plus, we all know that Joe Biden isn't ever going to give out free Goldfish crackers to everyone. 



Moving on, here's the output for my code, aka the comment count:
```
joannahwang@Joannas-MacBook-Pro code4bot % python3 bot_counter.py --username=anotha_bot   
len(comments)= 1000                    
len(top_level_comments)= 100
len(replies)= 900
len(valid_top_level_comments)= 0
len(not_self_replies)= 887
len(valid_replies)= 708
========================================
valid_comments= 708
========================================
NOTE: the number valid_comments is what will be used to determine your extra credit 
```

Mike, please note that you may get different numbers when running ```bot_counter.py```. I reached these numbers on 11/25 (I have a screenshot) and stopped running my bot for a bit before trying again in hopes of reaching 1000 comments. Unfortunately, that never happened. Now, I encounter weird errors, primarily 429 HTTP responses. 


# Grading 
1. Completing all tasks in the ```bot.py``` file - 18 pts
2. This repo - 2 pts
3. Got 100 valid comments - 2 pts
4. Got 500 valid comments - 2 pts
6. Made my bot reply to the most highly upvoted comment in a thread that it hasn't already replied to. You can see my code for this task by scrolling down to the      very bottom of my ```bot.py``` file. - 2 pts
7. Got my bot to upvote / downvote comments and submissions using TextBlob. See the ```bot_voting.py``` file. - 4 pts 

Based on the info above, I believe my score should be a **30/30**.

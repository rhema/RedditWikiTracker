# RedditWikiTracker
Scripts for saving a copy of Reddit wiki pages (e.g. for tracking automoderator).

PRAW is required and I should add a requirements.txt probablly. I use anaconda to manage this.

To run this script periodically, I use cron like so:
```
52 * * * * /home/rhema/anaconda3/envs/ufosbot/bin/python /home/rhema/code/RedditWikiTracker/track-wiki.py -s |.    /home/rhema/code/RedditWikiTracker/settings.json -sub ufos -o /home/rhema/code/r-ufos-automod/r-ufos-automoderator.txt
55 * * * * cd /home/rhema/code/r-ufos-automod && ./cron-push.sh
```

The first line initiates the conda environemnt and the second line runs an update script to a private repo.

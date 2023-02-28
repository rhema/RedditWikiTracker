import praw
import json
import time
import sys
import argparse

def cmdline_args():
        # Make parser object
    p = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    
    p.add_argument("-s", "--settings",
                   help="location of settings.json file with reddit login info")
    p.add_argument("-sub", "--subreddit",
                   help="location of settings.json file with reddit login info")
    p.add_argument("-o", "--outfile", default=None,
                   help="location of output file. If this argument is not specified, then it will simply print to the console.")
    p.add_argument("-w", "--wiki", default='config/automoderator',
                   help="relative location of the wiki page where the default is config/automoderator")
    return(p.parse_args())


if __name__ == '__main__':
    args = None
    if sys.version_info<(3,5,0):
        sys.stderr.write("You need python 3.5 or later to run this script\n")
        sys.exit(1)
    try:
        args = cmdline_args()
    except:
        print('Try $python track-wiki.py -s settings.json -sub ufos')
    #open settings file
    settings = json.load(open(args.settings))
    reddit = praw.Reddit(
        username=settings['username'],
        password=settings['password'],
        user_agent=settings['user_agent'],
        client_id=settings['client_id'],
        client_secret=settings['client_secret'])
    content = reddit.subreddit(args.subreddit).wiki[args.wiki].content_md
    if args.outfile is None:
        print(content)
    else:
        outfile = open(args.outfile,"w")
        outfile.write(content)
        outfile.close()
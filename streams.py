#!/usr/bin/env python
# -*- coding: utf-8 -*-

import praw
import re
from termcolor import colored, cprint
import sys


r = praw.Reddit(user_agent="Link Getter")


def login():
    r.login('stvhwrd', 'baby1o99', disable_warning=True)
    # Enter REDDIT USERNAME AND REDDIT PASSWORD
    # NEEDED TO SEARCH FOR ALL THE LINKS

    print(colored("Logging in...\n", 'yellow'))


def football_highlights():
    subreddit = r.get_subreddit("footballhighlights")

    for submission in subreddit.get_hot(limit=15):
        print("Highlight:", submission.title)

    highlight = input(colored("Which game highlights do you want?\n"))

    cprint("** HOLD COMMAND + CLICK to open link in browser **", 'red')

    for submission in subreddit.get_hot(limit=80):
        if re.search(highlight, submission.title, re.IGNORECASE):
            print("\nTitle: ", submission.title)
            print (submission.selftext)

            # Use this code below if you want to see the first comments
            # (generates more links)
            #
            # comments = submission.comments
            # for comment in comments[0:1]:  # first comment is a bot moderator
            #    print(comment.body)  # prints top comments starting from 2nd
            #    print("\n")

    restart_program()


def sport_links():
    subreddit = r.get_subreddit("soccerstreams")

    test = colored("Live games that you can stream...\n", 'yellow')
    print(test)

    for submission in subreddit.get_hot(limit=12):
        print("Game Name:", submission.title)

    print_input5 = colored("\n\nName of the game you want to watch: \n", 'red', attrs=['bold'])

    user_input = input(print_input5)
    cprint ("~~~~~~HOLD COMMAND + DOUBLE CLICK = Open link in browser ~~~~~~", 'red')

    for submission in subreddit.get_hot(limit=12):
        if re.search(user_input, submission.title, re.IGNORECASE):
            print("\nTitle: ", submission.title)
            print("Link: ", submission.url)
            print("Choose your link!")

            comments = submission.comments
            for comment in comments[1:3]:  # first comment is a bot moderator
                print(comment.body)  # prints top comments starting from 2nd top comment
                print("\n")

    restart_program()


def restart_program():
    # restart search if needed
    print_restart = colored("Do you need any other links?\n"
                            "Highlights 'h', Soccer Streams 's', Logout 'L', "
                            "Main Menu 'MM'\n", 'red', attrs=['bold'])

    restart = input(print_restart).lower()

    if (restart == "h"):
        football_highlights()
    elif (restart == "s"):
        sport_links()
    elif (restart == "l"):
        print("Bye")
        sys.exit()
    else:
        restart_program()

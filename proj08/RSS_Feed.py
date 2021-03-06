# Name:Damian and Bonnie
# Date:June 28th, 2017

import feedparser
import string
import time
from project_util import translate_html
from news_gui import Popup

#-----------------------------------------------------------------------
#
# proj08: RSS Feed Filter

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret

#======================
# Part 1
# Data structure design
#======================

# Problem 1

# TODO: NewsStory


class NewsStory(object):
    def __init__(self, guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link
    def get_guid(self):
        return self.guid
    def get_title(self):
        return self.title
    def get_subject(self):
        return self.subject
    def get_summary(self):
        return self.summary
    def get_link(self):
        return self.link



#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError


# Whole Word Triggers
# Problems 2-5

# TODO: WordTrigger
class WordTrigger(Trigger):
    def __init__(self, word):

        self.word = word.lower()


    def is_word_in(self, str):


        str = str.lower()
        #print str
        # upper/lower
        import string
        punctuation = string.punctuation

        for item in punctuation:
            str = str.replace(item, ' ')

        str = str.split(' ')
        #print str
        #print self.word
        if self.word in str:
            #print True#might be something wrong with 'story'
            return True
        else:
            return False










# TODO: TitleTrigger

class TitleTrigger(WordTrigger):

    def evaluate(self, story):


        return self.is_word_in(story.get_title())
# story not workin g










# TODO: SubjectTrigger
class SubjectTrigger(WordTrigger):

    def evaluate(self, story):

        return self.is_word_in(story.get_subject())



# TODO: SummaryTrigger

class SummaryTrigger(WordTrigger):

    def evaluate(self, story):

        return self.is_word_in(story.get_summary())

# class linktrigger(str):
#     def linktrigger(self, story):
#         if linktrigger in story:
#             return True
#         else:
#             return False

# Composite Triggers
# Problems 6-8

# TODO: NotTrigger
class NotTrigger(Trigger):

    def __init__(self, Trigger):
        self.Trigger = Trigger



    def evaluate(self, story):
        return not self.Trigger.evaluate(story)




# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, Trigger, Trigger2):
        self.Trigger = Trigger
        self.Trigger2 = Trigger2

    def evaluate(self, story):


            return self.Trigger.evaluate(story) and self.Trigger2.evaluate(story)





# TODO: OrTrigger

class OrTrigger(Trigger):
    def __init__(self, Trigger, Trigger2):
        self.Trigger = Trigger
        self.Trigger2 = Trigger2

    def evaluate(self, story):


            return self.Trigger.evaluate(story) or self.Trigger2.evaluate(story)


# Phrase Trigger
# Question 9

# TODO: PhraseTrigger

class PhraseTrigger(Trigger):


    def __init__(self, phrase):
        self.phrase = phrase


    def evaluate(self, story):

        #subject
        subject = story.get_subject()
        title = story.get_title()
        summary = story.get_summary()
        if self.phrase in subject or self.phrase in title or self.phrase in summary:
            return True
        else:
            return False



#======================
# Part 3
# Filtering
#======================

def filter_stories(stories, triggerlist):
    storylist = []
    for story in stories:
        for Trigger in triggerlist:
            if Trigger.evaluate(story):
                storylist.append(story)
    return storylist







    # """
    # Takes in a list of NewsStory-s.
    # Returns only those stories for whom
    # a trigger in triggerlist fires.
    # """
    # # TODO: Problem 10
    # This is a placeholder (we're just returning all the stories, with no filtering)
    # Feel free to change this line!


#======================
# Extensions: Part 4
# User-Specified Triggers
#======================

def readTriggerConfig(filename):
    # """
    # Returns a list of trigger objects
    # that correspond to the rules set
    # in the file filename
    # """
    # # Here's some code that we give you
    # # to read in the file and eliminate
    # # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    # TODO: Problem 11
    # 'lines' has a list of lines you need to parse
    # Build a set of triggers from it and
    # return the appropriate ones

import thread

def main_thread(p):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    t1 = SubjectTrigger("Trump")
    t2 = SummaryTrigger("Vanderbilt")
    t3 = PhraseTrigger("Net Neutrality")
    t4 = OrTrigger(t2, t3)
    triggerlist = [t1, t4]

    # TODO: Problem 11
    # After implementing readTriggerConfig, uncomment this line
    #triggerlist = readTriggerConfig("triggers.txt")

    guidShown = []

    while True:
        print "Polling..."

        # Get stories from Google's Top Stories RSS news feed
        stories = process("http://news.google.com/?output=rss")
        # Get stories from Yahoo's Top Stories RSS news feed
        stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

        # Only select stories we're interested in
        stories = filter_stories(stories, triggerlist)

        # Don't print a story if we have already printed it before
        newstories = []
        for story in stories:
            if story.get_guid() not in guidShown:
                newstories.append(story)
        
        for story in newstories:
            guidShown.append(story.get_guid())
            p.newWindow(story)

        print "Sleeping..."
        time.sleep(SLEEPTIME)

SLEEPTIME = 60 #seconds -- how often we poll
if __name__ == '__main__':
    p = Popup()
    thread.start_new_thread(main_thread, (p,))
    p.start()


# Name:
# Date:

# proj07: Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k':
        5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u':
        1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    stringlist = []
    letterlist = []
    comparedlist = {}





#take every letter in their wordOK
#check what every letter is worth
#add up what all the letters are worth
#multiply that by length(word)


    #wordinput = raw_input ("Enter your word!")
    score = 0
    letterlist=[]
    for letters in word:
        score = score + SCRABBLE_LETTER_VALUES[letters]
        letterlist.append(letters)
    wordlength = len(letterlist)
    wordscore = score*wordlength
    print score, " is the score before mutiplying"
    print wordscore, "is after multiplying"
    print letterlist

    # stringlist.append(word)
    # for letters in letterlist:
    #     if letters in letterlist:
    #         print "if state worked"
    # index=0
    # for key in SCRABBLE_LETTER_VALUES:
    #     if key in letterlist:
    #         comparedlist = letterlist.copy()
    #         print comparedlist
    #SCRABBLE_LETTER_VALUES
    return word
get_word_score("hello", 10)

"""
    Returns the score for a word. Assumes the word is a
    valid word.

	The score for a word is the sum of the points for letters
	in the word multiplied by the length of the word, plus 50
	points if all n letters are used on the first go.

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    # TO DO...
    
#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#hand down below is ony a placeholder. pretend "hand" actually does represent something


def update_hand(hand, word):

    new_hand = hand.copy()


    leftoverletters = {}
    letterlist2 = {}
    for letters in word:
        letterlist2.append(letters)

    for letters in hand:
        if letters not in letterlist2:
            get.frequency_dict(letters)
    print leftoverletters, "these are the letters you ave left and can still use"



    return new_hand




    leftoverletters=[]
    letterlist2 = []
    for letters in word:
        letterlist2.append(letters)

    for letters in hand:
        if letters not in letterlist2:
            leftoverletters.append(letters)

    print leftoverletters, "these are the letters you have left and can still use"
    return leftoverletters
update_hand(deal_hand(HAND_SIZE), "hello")




#letterlist has the words entered by player
    # """
    # Assumes that 'hand' has all the letters in word.
    # In other words, this assumes that however many times
    # a letter appears in 'word', 'hand' has at least as
    # many of that letter in it.
    #
    # Updates the hand: uses up the letters in the given word
    # and returns the new hand, without those letters in it.
    #
    # Has no side effects: does not modify hand.
    #
    # word: string
    # hand: dictionary (string -> int)
    # returns: dictionary (string -> int)
    # """
    # TO DO ...

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    letterlist3 = []
    for letters in word:
        letterlist3.append(letters)
    number = 0
    number2 = 0

    if word not in word_list:
        print "invalid word. not in word list."
    if word in word_list:
        print "valid word. in word list. good job"



    for letters in word:
        if letters in letterlist3:
            number2 = number2 + 1

        if letters in hand:
            number = number +1#letter has not been used before
            print "good one!"


        elif letters not in hand:
            print "terrible! you used a letter you dont have. >:("
            return False
    if number < number2:
        return False

    return True






#is_valid_word("hello",deal_hand(HAND_SIZE), load_words())







    # TO DO...

def calculate_handlen(hand):
    handlen = 0
    for v in hand.values():
        handlen += v
    return handlen

#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      
    """
    # TO DO ...

#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # TO DO...

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)




























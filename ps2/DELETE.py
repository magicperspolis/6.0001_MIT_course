# wordlist=['ad', 'am', 'an', 'as', 'at', 'ax', 'be', 'by', 'do', 'em', 'en', 'ex', 'go', 'he', 'hi', 'ho', 'if', 'in',
#           'is', 'it', 'me', 'my', 'no', 'of', 'oh', 'on', 'or', 'ox', 'pi', 're', 'so', 'to', 'up', 'us', 'we', 'ye',
#           'ace', 'act', 'add', 'ado', 'ads', 'adz', 'aft', 'age', 'ago', 'aid', 'ail', 'aim', 'air', 'alb', 'ale',
#           'all', 'and', 'ant', 'any', 'ape', 'apt', 'arc', 'are', 'ark', 'arm', 'art', 'ash', 'ask', 'asp', 'ass',
#           'ate',  'ave', 'awe', 'awl', 'awn', 'aye', 'bad', 'bag', 'bah', 'ban', 'bar', 'bat', 'bay', 'bed', 'bee',
#           'beg',  'bel', 'bet', 'bib', 'bid', 'big', 'bin', 'bit', 'boa', 'bob', 'bog', 'boo', 'bop', 'bow', 'box',
#           'boy',  'bra', 'bud', 'bug', 'bum', 'bun', 'bur', 'bus', 'but', 'buy', 'bye', 'cad', 'cam', 'can', 'cap',
#           'car',  'cat', 'cay', 'chi', 'cob', 'cod', 'cog', 'con', 'coo', 'cop', 'cot', 'cow', 'coy', 'cry', 'cub',
#           'cud',  'cue', 'cup', 'cur', 'cut', 'dad', 'dam', 'daw', 'day', 'den', 'dew', 'did', 'die', 'dig', 'dim',
#           'din',  'dip', 'doe', 'dog', 'don', 'dot', 'dry', 'dub', 'dud', 'due', 'dug', 'dun', 'duo', 'dye', 'ear',
#           'eat',  'ebb', 'eel', 'egg', 'ego', 'eke', 'elf', 'elk', 'ell', 'elm', 'end', 'eon', 'era', 'erg', 'err',
#           'eve',  'ewe', 'eye', 'fad', 'fag', 'fan', 'far', 'fat', 'fed', 'fee', 'fen', 'few', 'fey', 'fez', 'fib',
#           'fie',  'fig', 'fin', 'fir', 'fit', 'fix', 'flu', 'fly', 'fob', 'foe', 'fog', 'fop', 'for', 'fox', 'fro',
#           'fry',  'fun', 'fur', 'gad', 'gag', 'gal', 'gam', 'gap', 'gar', 'gas', 'gay', 'gel', 'gem', 'get', 'gig',
#           'gin',  'gnu', 'gob', 'god', 'goo', 'got', 'gum', 'gun', 'gut', 'guy', 'gym', 'gyp', 'had', 'hag', 'ham',
#           'hap',  'has', 'hat', 'haw', 'hay', 'hem', 'hen', 'her', 'hew', 'hex', 'hey', 'hid', 'hie', 'him', 'hip',
#           'his',  'hit', 'hob', 'hoc', 'hod', 'hoe', 'hog', 'hop', 'hot', 'how', 'hub', 'hue', 'hug', 'hum', 'hun',
#           'hut',  'ice', 'icy', 'ids', 'ifs', 'ilk', 'ill', 'imp', 'ink', 'inn', 'ins', 'ion', 'ire', 'irk', 'its',
#           'ivy',  'jag', 'jam', 'jar', 'jaw', 'jay', 'jet', 'jew', 'jib', 'jig', 'job', 'jog', 'jot', 'joy', 'jug',
#           'jut',  'keg', 'ken', 'key', 'kid', 'kin', 'kip', 'kit', 'lac', 'lad', 'lag', 'lao', 'lap', 'law', 'lax',
#           'lay',  'lea', 'led', 'lee', 'leg', 'lei', 'leo']

# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()







def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word_no_space=''
    for letter in my_word:
        if not letter==' ':
            my_word_no_space=my_word_no_space+letter

    if len(my_word_no_space)==len(other_word):
        for n in range(0,len(my_word_no_space),1):
            if str.isalpha(my_word_no_space[n]):
                if not my_word_no_space[n]==other_word[n]:
                    return False
        return True
    return False

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    local_counter=0
    for n in range(0,len(wordlist),1):
        other_word=wordlist[n]
        if match_with_gaps(my_word,other_word):
            print(other_word)
            local_counter+=1
    if not local_counter>0:
        print('No matches found')







show_possible_matches('a_ pl_ ')
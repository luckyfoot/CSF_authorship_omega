'''
Welcome to the Authorship project by Antonio (luckyfoot) and Rosemary (in-verse)

We'd like to give thanks to the many classmates who've helped us with this project.
Appreciation to Alexia for the idea behind a helper function for splitting words,
to Sam for guidance on signature comparison, and to Isaak for teaching us about
functional programming with lambda.
'''

import os.path, math
import re


def clean_up(s):
    ''' Return a version of string s in which all letters have been
    converted to lowercase and punctuation characters have been stripped
    from both ends. Inner punctuation is left untouched. '''

    punctuation = '''!"',;:.-?)([]<>*#\n\t\r'''
    result = s.lower().strip(punctuation)
    return result


# HELPER FUNCTIONS ---------------------------------------------------------------------

def take_words(text):
    ''' Helper function that takes in string, text, and then splits them on characters
    that aren't from the alphabet. Finally, it filters.'''

    split_text = clean_up(''.join(text))
    split_text = re.sub('\s+', ' ', split_text) # \s looks for non-whitespace character in [^ \t\n\r\f\v] , + allows repetitions
    words = re.split("[!|?|.|,|:)|' ']+", split_text)  # Pipe through splitting by regular expressions
    list_of_words = list(filter(None, words)) # Filters and creates a list

    return list_of_words

def take_sentences(text):
    '''Returns a list containing sentences. Original string/list is
    separated, cleaned, and split.'''

    sentences_list = ''.join(text)  # Joins array into a string and does nothing if input is already a string
    sentences_list = clean_up(''.join(sentences_list))
    sentences_list = re.sub('\s+', ' ', sentences_list) # Removes \n
    sentences = re.split("""[?!.]+""", sentences_list) # Splits alongside ?,!, and .

    return sentences

# LINGUISTIC FEATURES --------------------------------------------------------------------


def type_token_ratio(text):
    ''' Return the type token ratio (TTR) for this text.
    TTR is the number of different words divided by the total number of words.
    text is a non-empty list of strings each ending in \n.
    At least one line in text contains a word. '''

    word_count = 0
    unq_words = 0

    list_of_words = take_words(text)
    single_words = list_of_words[:]  # Makes a string copy of words to check list_of_words by
    for a_word in list_of_words:
        word_count += 1
        while single_words.count(a_word) > 1:
            single_words.remove(a_word)
    for word in single_words:
        unq_words += 1
    ttr = unq_words / word_count
    return ttr


def hapax_legomana_ratio(text):
    ''' Return the hapax_legomana ratio for this text.
    This ratio is the number of words that occur exactly once divided
    by the total number of words.
    text is a list of strings each ending in \n.
    At least one line in text contains a word.'''

    word_count = 0
    unq_word = 0
    list_of_words = take_words(text)

    for a_word in list_of_words:
        word_count += 1
        if list_of_words.count(a_word) == 1:
            unq_word += 1

    hlr = unq_word / word_count
    return hlr

def avg_sentence_complexity(text):
    '''Return the average number of phrases per sentence.
    Terminating punctuation defined as !?.
    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation
    or beginning or end of file.
    Phrases are substrings of a sentences separated by
    one or more of the following delimiters ,;: '''

    # Cleaning block will return a list of sentences without extraneous junk
    clean_list = []
    frag_list = []
    count_sentence = 0
    count_phrase = 0

    cleaned_sentence = clean_up(''.join(text))
    sentences = re.split("""[?!.]+""", cleaned_sentence)

    for word in sentences:  # Double checking for all words to be greater than 1
        if len(word) > 1:
            clean_list.append(word)

    for line in clean_list:
        if (':' in line) or (',' in line) or (';' in line):
            frag_list = frag_list + re.split("[:|;|,]", line) # Create a list that takes phrases from ':',';', and ','
        else:
            frag_list.append(line) # Also want to include a sentence because 1 sentence by itself = 1 phrase

    for sentence in clean_list:
        count_sentence += 1
    for phrase in frag_list:
        count_phrase += 1

    avg_sentence_complexity = count_phrase / count_sentence
    return avg_sentence_complexity

def average_sentence_length(text):
    ''' Return the average number of words per sentence in text.
    text is guaranteed to have at least one sentence.
    Terminating punctuation defined as !?.
    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation
    or beginning or end of file. '''

    #Declare variables to place sentences after extraneous stuff is removed

    clean_list = []
    num_words = 0

    sentences = take_sentences(text)

    for line in sentences: # Populate clean list and double check that each element is not a empty string, ''
        if len(line) > 1:
            clean_list.append(line)

    num_sentences = len(clean_list)

    for sentence in clean_list:
        counter = sentence.split()
        for word in counter:

            if word[0].isalpha() == True: # Checks 0th position of word to see if it's alphabet, if so - its counted as a word
                num_words += 1
    asl = num_words / num_sentences
    return asl

def average_word_length(text):
    """ Returns the average length of all words in the string """
    num_letters = 0
    num_words = 0

    word_list = take_words(text)
    num_words = len(word_list) # Number of words is equal to number of elements in list

    num_letters = 0
    for a_word in word_list: # Number of letters is the number of characters in each word
        num_letters += len(a_word)

    average_word_length = num_letters / num_words
    return average_word_length

# --------------------------------------------------------------------------------------

def get_valid_filename(prompt):
    '''Use prompt (a string) to ask the user to type the name of a file. If
    the file does not exist, keep asking until they give a valid filename.
    The filename must include the path to the file.
    Return the name of that file.'''

    # To do: Complete this function's body to meet its specification.
    # use: print ("That file does not exist: " + filename)
    # Do not use any other input or output statements in this function.

    control = False
    while control != True:
        filename = input(prompt)
        try:
            test = open(filename)
            test.close()
            control = True
        except IOError:
            print('That file does not exist: ', filename)

    return filename


def read_directory_name(prompt):
    '''Use prompt (a string) to ask the user to type the name of a directory. If
    the directory does not exist, keep asking until they give a valid directory.
    '''

    # To do: Complete this function's body to meet its specification.
    # use print ("That directory does not exist: " + dirname)
    control = False
    while control != True:
        dirname = input(prompt)
        control = os.path.isdir(dirname)
        if control == False:
            print("That directory does not exist: ", dirname)

    return dirname


# COMPARE SIGNATURES -------------------------------------------------------------------

def compare_signatures(sig1, sig2, weight):
    '''Return a non-negative real number indicating the similarity of two
    linguistic signatures. The smaller the number the more similar the
    signatures. Zero indicates identical signatures.
    sig1 and sig2 are 6 element lists with the following elements
    0  : author name (a string)
    1  : average word length (float)
    2  : TTR (float)
    3  : Hapax Legomana Ratio (float)
    4  : average sentence length (float)
    5  : average sentence complexity (float)
    weight is a list of multiplicative weights to apply to each
    linguistic feature. weight[0] is ignored.
    '''
    sig = 0
    pos = 1
    while pos < 6: # Happens 5 times
        sig += abs(sig1[pos] - sig2[pos]) * weight[pos]
        pos += 1
    return sig


def read_signature(filename):
    '''Read a linguistic signature from filename and return it as
    list of features. '''

    file = open(filename, 'r') # Read file
    result = [file.readline()]
    for line in file:
        result.append(float(line.strip()))
    return result


if __name__ == '__main__':

    prompt = 'enter the name of the file with unknown author:'
    mystery_filename = get_valid_filename(prompt)

    # readlines gives us a list of strings one for each line of the file
    text = open(mystery_filename, 'r').readlines()

    # calculate the signature for the mystery file
    mystery_signature = [mystery_filename]
    mystery_signature.append(average_word_length(text))
    mystery_signature.append(type_token_ratio(text))
    mystery_signature.append(hapax_legomana_ratio(text))
    mystery_signature.append(average_sentence_length(text))
    mystery_signature.append(avg_sentence_complexity(text))

    weights = [0, 11, 33, 50, 0.4, 4]

    prompt = 'enter the path to the directory of signature files: '
    dir = read_directory_name(prompt)
    # every file in this directory must be a linguistic signature
    files = os.listdir(dir)

    # we will assume that there is at least one signature in that directory
    this_file = files[0]
    signature = read_signature('%s/%s' % (dir, this_file))
    best_score = compare_signatures(mystery_signature, signature, weights)
    best_author = signature[0]
    for this_file in files[1:]:
        signature = read_signature('%s/%s' % (dir, this_file))
        score = compare_signatures(mystery_signature, signature, weights)
        if score < best_score:
            best_score = score
            best_author = signature[0]
    print("best author match: %s with score %s" % (best_author, best_score))

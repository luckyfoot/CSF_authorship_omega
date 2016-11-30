import os.path, math
import re

def clean_up(s):
    ''' Return a version of string s in which all letters have been
    converted to lowercase and punctuation characters have been stripped 
    from both ends. Inner punctuation is left untouched. '''
    
    punctuation = '''!"',;:.-?)([]<>*#\n\t\r'''
    result = s.lower().strip(punctuation)
    return result

def take_words(text):
    ''' Helpter function that takes in string, text, and then splits them on characters
    that aren't from the alphabet. Finally, it filters.'''
    split_text = ''.join(text)
    split_text = split_text.replace(r'\n', ' ')
    words = re.split("[!|?|.|,|:)|' ']+", split_text)  # aka. ('\s|(?<!\d)[,.]|[,.](?!\d) or [^\w']+
    list_of_words = list(filter(None, words))
    return list_of_words
    
def average_word_length(text):
    ''' Return the average length of all words in text. Do not
    include surrounding punctuation in words.
    text is a non-empty list of strings each ending in \n.
    At least one line in text contains a word.'''
    text_clean = take_words(text)
    word_list = []
    total_sum = 0
    word_total = 0
    for word in text_clean:
        if len(word) > 0:
            word_list.append(word)
            word_total += 1
    for word in word_list:
        total_sum += len(word)
    awl = total_sum / word_total
    return awl
    
def type_token_ratio(text):
    ''' Return the type token ratio (TTR) for this text.
    TTR is the number of different words divided by the total number of words.
    text is a non-empty list of strings each ending in \n.
    At least one line in text contains a word. '''
    
    word_count = 0
    unq_words = 0
    
    text_str = ''.join(text)
    text_str = text_str.replace('\n', ' ')
    words = re.split("[!|?|.|,|:)]", text_str)
    text_str = ''.join(words)
    words = text_str.split()
    single_words = words[:]
    
    for w in words:
        word_count += 1
        while single_words.count(w) > 1:
            single_words.remove(w)
    for w in single_words:
        unq_words += 1
    ttr = unq_words/word_count
           
    return  ttr 
    
                
def hapax_legomana_ratio(text):
    ''' Return the hapax_legomana ratio for this text.
    This ratio is the number of words that occur exactly once divided
    by the total number of words.
    text is a list of strings each ending in \n.
    At least one line in text contains a word.'''

    word_count = 0
    unq_word = 0
    text_str = ''.join(text)
    text_str = text_str.replace('\n', ' ')
    words = re.split("[!|?|.|,|:)]", text_str)
    text_str = ''.join(words)
    words = text_str.split()   

    for w in words:
        word_count += 1
        if words.count(w) == 1:
            unq_word += 1

    hlr = unq_word / word_count    
    
    return hlr

'''
You don't need this function.
you can use re.split(), where you give it a regular expression.
Regular expressions include '[!\?\.]'
def split_on_separators(original, separators):
     Return a list of non-empty, non-blank strings from the original string
    determined by splitting the string on any of the separators.
    separators is a string of single-character separators.
'''   
    
def average_sentence_length(text):
    ''' Return the average number of words per sentence in text.
    text is guaranteed to have at least one sentence.
    Terminating punctuation defined as !?.
    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation
    or beginning or end of file. '''
    '''
    declare variable to place sentances after extrenous
    stuff is removed and word count variable
    '''
    clean_list = []
    num_words = 0
    
    #cleaning block will return a list of sentances without extranous junk
    text_str = ''.join(text)
    text_str = text_str.replace('\n', ' ')
    split_list = re.split("[.|?|!]", text_str)

    #populate clean list 
    for line in split_list:
        if len(line) > 1 :
            clean_list.append(line)
            
    num_sentances = len(clean_list) 

    for sentance in clean_list:
        counter = sentance.split()
        for word in counter:
            if word.isalpha() == True:
                num_words += 1
    asl = num_words / num_sentances
    
    return asl
    

def avg_sentence_complexity(text):
    '''Return the average number of phrases per sentence.
    Terminating punctuation defined as !?.
    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation
    or beginning or end of file.
    Phrases are substrings of a sentences separated by
    one or more of the following delimiters ,;: '''
    #cleaning block will return a list of sentances without extranous junk
    clean_list = []
    frag_list =[]
    count_sentence = 0
    count_phrase = 0
    text_str = ''.join(text)
    list_sent = re.split("[.|!|?]",text_str)
    for ele in list_sent:
        if len(ele) > 1 :
            clean_list.append(ele)
    for line in clean_list:
        frag_list = re.split("[:|;|,]",line)
    try:
        for line in clean_list:
            if frag_list.count(line) == 0:
                frag_list.append(line)
    except:
        print('Invalid line')
    for sentence in clean_list:
        count_sentence += 1
    for phrase in frag_list:
        count_phrase += 1
    avg_sentence_complexity = count_phrase / count_sentence
    return avg_sentence_complexity
    
    
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
            print ('That file does not exist: ', filename)
        
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
            print ("That directory does not exist: ", dirname)
            
    return dirname

    
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
    while pos < 6:
        sig += abs(sig1[pos]-sig2[pos])*weight[pos]
        pos +=1 
    return sig
    

def read_signature(filename):
    '''Read a linguistic signature from filename and return it as 
    list of features. '''
    
    file = open(filename, 'r')
    # the first feature is a string so it doesn't need casting to float
    result = [file.readline()]
    # all remaining features are real numbers
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
    signature = read_signature('%s/%s'%(dir,this_file))
    best_score = compare_signatures(mystery_signature, signature, weights)
    best_author = signature[0]
    for this_file in files[1:]:
        signature = read_signature('%s/%s'%(dir, this_file))
        score = compare_signatures(mystery_signature, signature, weights)
        if score < best_score:
            best_score = score
            best_author = signature[0]
    print ("best author match: %s with score %s"%(best_author, best_score))
    

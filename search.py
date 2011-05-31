from simplejson import dumps, loads
from httplib2 import Http
from sys import argv

# Do the domai.nr search on given word
def do_search(word):
    client = Http()
    
    url = "http://domai.nr/api/json/search?q=%s" % (word,)
    resp, content = client.request(url)
    
    result = loads(content)
    
    try:
        if result['error']:
            return "domai.nr error: %s - %s" % (result['error']['status'], result['error']['message'],)
    except:
        return result['results'][0]['availability'];     

# Convert the word to l337 speak
def convertToLeetSpeak(word):
    leet_string = ''
    for c in word:
        if c == 'e' or c == 'E':
            leet_string += '3'
        elif c == 'a' or c == 'A':
            leet_string += '4'
        elif c == 't' or c == 'T':
            leet_string += '7'
        elif c == 's' or c == 'S':
            leet_string += '5'
        elif c == 'o' or c == 'O':
            leet_string += '0'
        else:
            leet_string += c
                
    return leet_string

try:    
    word_file = argv[1]

    f = open(word_file, 'r')
    all_words = map(lambda l: l.split(" "), f.readlines())

    for words in all_words:
        for w in words:
            if w != '' and w != "\n":
                leet_w = convertToLeetSpeak(w)
                print "The domain %s.com is: %s" % (leet_w, do_search(leet_w),)

except IndexError:
    print "Please supply a filename."

except IOError:
    print "Please supply a valid filename."
            

import snscrape.modules.twitter as sntwitter
import pandas as pd
import csv
#import nltk
#from nltk.corpus import stopwords //not needed because we hardcoded the library
import string

def tweets(query, since, until):
    parameter = query+" until:"+until+" since:"+since+" -filter:replies"
    tweets = []
    #limit = 5
    tweet_count=0

    #print("hello")
    for tweet in sntwitter.TwitterSearchScraper(parameter).get_items(): #get tweets

        tweets.append([tweet.date, tweet.user.username, tweet.content+" qqqqq", tweet.likeCount, tweet.replyCount, tweet.retweetCount, tweet.quoteCount])
        # print(vars(tweet))
        # break
        """""
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.date, tweet.user.username, tweet.content+" qqqqq", tweet.likeCount, tweet.replyCount, tweet.retweetCount, tweet.quoteCount])
        """""
        tweet_count += 1


    df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet', 'Like', 'Reply', 'Retweet', 'Quote' ]) #save list tweets into df with the headers named by columns
    """
    print(df)
    print("hello")
    """

    # to save to tweets.csv
    df.to_csv('tweets.csv')

    words = []
    words_counted = []
    current_words = []

    with open('tweets.csv', 'rt', encoding="utf8") as csvfile: #gather words
        reader = csv.reader(csvfile)
        #next(reader)
        for col in reader:
            csv_words = col[3].split(" ")
            #csv_words.pop(0)
            for i in csv_words:
                if i != "qqqqq": #used to separate tweets since the .split method just separates by word and adds them all into a single list
                    i = i.translate(str.maketrans('', '', string.punctuation))
                    if i not in current_words:
                        words.append(i.lower()) #lowerkey to make comparing easier
                        current_words.append(i.lower()) #current_words is to make sure duplicates of a word in a single tweet are counted
                else:
                    current_words=[]
                #print(i)

    english_stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "dont", "should", "now","via", "us", "see", "instead", "really", "what", "dzrhnews", "todays", "today", "gave", "wanna", "Dr", "ad", "mwa", "exp", "made", "also", "says", "say", "let", "really", "instead", "im", "i’m", "oh", "could", "5", "shes", "sir", "miss", "dont", "yes", "thats", "much", "many", "haha", "sure", "c", "it’s", "since", "e", "cant", "can’t", "won’t", "well", "hahahaha", "ever", "guys", "mrs", "every", "mrs.", "mr.", "ms.", "though", "others", "accdg", "according", "atm", "doc", "indeed", "especially", "hehe", "wait", "thats", "pls", "neither", "okay", "ok", "dont", "don’t", "yet", "almost", "wont", "go", "goes", "went", "lets"]
    filo_stop_words = ["a", "akin", "aking", "ako", "alin", "am", "amin", "aming", "amp", "ang", "ano", "anumang", "apat", "at", "atin", "ating", "ay", "bababa", "bago", "bakit", "bawat", "bilang", "dahil", "dalawa", "dapat", "din", "dito", "doon", "eh", "gagawin", "gayunman", "ginagawa", "ginawa", "ginawang", "gumawa", "gusto", "habang", "hanggang","hindi","huwag","iba","ibaba", "ibabaw", "ibig","ikaw", "ilagay", "ilalim", "ilan", "ilang", "inyong", "isa", "isang", "itaas", "ito", "iyo", "iyon", "iyong", "ka", "kahit", "kailangan", "kailanman", "kami", "kanila", "kanilang", "kanino", "kanya", "kanyang", "kapag", "kapwa", "karamihan", "katiyakan", "katulad", "kay", "kaya", "kayo", "kaysa", "ko", "kong", "kulang", "kumuha", "kung", "laban", "lahat", "lamang", "lang", "likod", "lima", "maaari", "maaaring", "maging", "mahusay", "makita", "marami", "marapat", "mas", "masyado", "may", "mayroon", "mga", "minsan", "mismo", "mo", "mong", "mula", "muli", "na", "nag", "nabanggit", "naging", "nagkaroon", "nais", "nakita", "namin", "napaka", "narito", "nasaan", "ng", "ngayon", "ni", "nila", "nilang", "nito", "niya", "niyang", "noon", "o", "pa", "paano", "pababa", "paggawa", "pagitan", "pagkakaroon", "pagkatapos", "palabas", "pamamagitan", "panahon", "pangalawa", "para", "paraan", "pareho", "pataas", "pero", "po", "pumunta", "pumupunta", "sa", "saan", "sabi", "sabihin", "sarili", "si", "sila", "sino", "siya", "tatlo", "tayo", "tulad", "tungkol", "una", "walang", "yung", "naman", "natin", "ba", "talaga", "di", "nyo", "pag", "daw", "nya", "wala", "nga", "sya", "yan", "niyo", "mag", "kasi", "rin", "nang", "sana", "nung", "alam", "pala", "baka", "wag", "ung", "parang", "nasa", "nina", "ibang", "pang", "san", "grabe", "sina", "sayo", "u", "nalang", "nitong", "ilang", "tayong", "akong", "inyo", "kasama", "g", "n","yun", "muna", "sinabi", "sobra", "sobrang", "nating", "kanina", "pati", "ganun", "ha", "naka", "puro", "talagang", "tlg", "silang", "kaniyang", "upang", "taga", "de", "parin", "noong", "eto", "kundi", "bang", "pagka", "‘to", "la", "tas", "hahahahahha", "sakin", "kina", "pong", "ayon", "agad", "un", "buhy", "diba", "lt3", "yong", "pano", "yon", "lalong", "r", "siyang", "etong", "biglang", "kayong", "tong", "dyan", "charot", "kang", "kabila", "dala", "yt", "edga", "httpstco5jvtt31tig", "sinong", "pinag", "away", "httpstcoyqlhrzkcs7", "gaano", "basta", "kana", "samin", "naten", "siguro", "kagaya", "cppnpandf", "paki", "luh", "satin", "nyong", "kaninang", "mu", "ang", "lols", "hinde", "x", "padin", "talagang"]
    tweets_nsw = [] #nsw stands for no stop words
    remove_query=query.split(" ")#remove the query from the results
    for w in words: #removes stop words
        if w not in english_stop_words:
            if w != '':
                if w not in filo_stop_words:
                    if w not in remove_query:
                        tweets_nsw.append(w)
    #print(words)
    #print(tweets_nsw)

    with open('frequency_result.csv',  'w',newline='', encoding="utf8") as csvfile: #save words into frequency_result csv file
        writer = csv.writer(csvfile, delimiter=',')
        for i in tweets_nsw:
            x = tweets_nsw.count(i)
            y = (x/tweet_count)*100
            words_counted.append((i,x,y))
        words_counted = list(dict.fromkeys(words_counted))
        words_counted=sorted(words_counted, key = lambda x: x[1], reverse=True) #to sort the list based on x[1] so index 1 which holds the word usage count, can use index 2 i thnk as well
        writer.writerows(words_counted)

    '''this part shows the top 3 tweets'''
    sorted_tweets=sorted(tweets, key = lambda x: x[3], reverse=True) #sort list tweets by index 3 which has the like count
    string1=' '.join([str(item) for item in sorted_tweets[0]])
    string2=' '.join([str(item) for item in sorted_tweets[1]])
    string3=' '.join([str(item) for item in sorted_tweets[2]])
    string4 = "Total Tweet count: " + str(tweet_count) + "\nTop 3 tweets:\n" + string1 + "\n" +string2 + "\n" + string3
    return string4


import json
import pandas as pd
from textblob import TextBlob

def read_json(json_file: str)->list:
    """
    json file reader to open and read json files into a list
    Args:
    -----
    json_file: str - path of a json file
    
    Returns
    -------
    length of the json file and a list of json
    """
    
    tweets_data = []
    for tweets in open(json_file,'r'):
        tweets_data.append(json.loads(tweets))
    
    
    return len(tweets_data), tweets_data

class TweetDfExtractor:
    """
    this function will parse tweets json into a pandas dataframe
    
    Return
    ------
    dataframe
    """
    def __init__(self, tweets_list):
        
        self.tweets_list = tweets_list

    # an example function
    def find_statuses_count(self)->list:
        statuses_count = len(self.tweets_list['status'])
        
    def find_full_text(self)->list:
        text = []
        for i in self.tweets_list:
            try:
                text.append(i['text'])
            except KeyError:
                text.append(None)

        return text
       
    
    def find_sentiments(self, text)->list:
        
        return polarity, self.subjectivity

    def find_created_time(self)->list:
       created_at = []
        for i in self.tweets_list:
            try:
                created_at.append(i['created_at'])
            except KeyError:
                created_at.append(None)

        return created_at

    def find_source(self)->list:
        source = []
        for i in self.tweets_list:
            try:
                source.append(i['source'])
            except KeyError:
                source.append(None)

        return source

    def find_screen_name(self)->list:
        screen_name = []
        for i in self.tweets_list:
            try:
                screen_name.append(i['user']['screen_name'])
            except KeyError:
                screen_name.append(None)

        return screen_name

    def find_followers_count(self)->list:
        followers_count = 0
        for i in self.tweets_list:
            try:
                followers_count += i['followers_count']
            except KeyError:
                followers_count += 0
        return followers_count

    def find_friends_count(self)->list:
        friends_count = 0
        for i in self.tweets_list:
            try:
                friends_count += i['friends_count']
            except KeyError:
                friends_count += 0
        return friends_count

    def is_sensitive(self)->list:
        try:
            is_sensitive = [x['possibly_sensitive'] for x in self.tweets_list]
        except KeyError:
            is_sensitive = None

        return is_sensitive

    def find_favourite_count(self)->list:
        favourite_count = 0
        for i in self.tweets_list:
            try:
                favourite_count += i['favourite_count']
            except KeyError:
                favourite_count += 0
        return favourite_count
    
    def find_retweet_count(self)->list:
        retweet_count = 0
        for i in self.tweets_list:
            try:
                retweet_count += i['retweet_count']
            except KeyError:
                retweet_count += 0
        return retweet_count

    def find_hashtags(self)->list:
        hashtags = []
        for i in self.tweets_list:
            try:
                hashtags.append(i['entities']['hashtags']['text'])
            except KeyError:
                hashtags.append(None)
        return hashtags

    def find_mentions(self)->list:
        mentions = []
        for i in self.tweets_list:
            try:
                mentions.append(i['entities']['user_mentions']['name']) 
            except KeyError:
                mentions.append(None)
        return mentions
        
    def find_location(self)->list:
        try:
            location = self.tweets_list['user']['location']
        except TypeError:
            location = ''
        
        return location

    
        
        
    def get_tweet_df(self, save=False)->pd.DataFrame:
        """required column to be generated you should be creative and add more features"""
        
        columns = ['created_at', 'source', 'original_text','polarity','subjectivity', 'lang', 'favorite_count', 'retweet_count', 
            'original_author', 'followers_count','friends_count','possibly_sensitive', 'hashtags', 'user_mentions', 'place']
        
        created_at = self.find_created_time()
        source = self.find_source()
        text = self.find_full_text()
        polarity, subjectivity = self.find_sentiments(text)
        lang = self.find_lang()
        fav_count = self.find_favourite_count()
        retweet_count = self.find_retweet_count()
        screen_name = self.find_screen_name()
        follower_count = self.find_followers_count()
        friends_count = self.find_friends_count()
        sensitivity = self.is_sensitive()
        hashtags = self.find_hashtags()
        mentions = self.find_mentions()
        location = self.find_location()
        data = zip(created_at, source, text, polarity, subjectivity, lang, fav_count, retweet_count, screen_name, follower_count, friends_count, sensitivity, hashtags, mentions, location)
        df = pd.DataFrame(data=data, columns=columns)

        if save:
            df.to_csv('processed_tweet_data.csv', index=False)
            print('File Successfully Saved.!!!')
        
        return df

                
if __name__ == "__main__":
    # required column to be generated you should be creative and add more features
    columns = ['created_at', 'source', 'original_text','clean_text', 'sentiment','polarity','subjectivity', 'lang', 'favorite_count', 'retweet_count', 
    'original_author', 'screen_count', 'followers_count','friends_count','possibly_sensitive', 'hashtags', 'user_mentions', 'place', 'place_coord_boundaries']
    _, tweet_list = read_json("../covid19.json")
    tweet = TweetDfExtractor(tweet_list)
    tweet_df = tweet.get_tweet_df() 

    # use all defined functions to generate a dataframe with the specified columns above

    
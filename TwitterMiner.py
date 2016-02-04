from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

token = ""
token_secret = ""
key = ""
key_secret = ""

class TweetsToStdOut(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    object = TweetsToStdOut()
    auth = OAuthHandler(key,key_secret)
    auth.set_access_token(token,token_secret)
    stream = Stream(auth,object)

stream.filter(track=['google'])

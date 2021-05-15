from tweepy.streaming import StreamListener


class CustomStreamListener(StreamListener):
    def __init__(self, db, max_count=10):
        super().__init__()
        self.db = db
        self.max_count = max_count
        self.count = 0

    def on_status(self, status):
        tweet = status._json
        print('tweet:', status.text)
        try:
            self.db[tweet['id_str']] = tweet
            self.count += 1
            if self.count >= self.max_count:
                return False
        except:
            pass

    def on_error(self, status_code):
        print(status_code)
        return True


from tweepy.streaming import StreamListener


class CustomStreamListener(StreamListener):
    def __init__(self, db,keyword, location, max_count=10):
        super().__init__()
        self.db=db
        self.max_count = max_count
        self.count = 0
        self.keyword = keyword
        self.location = location

    def on_status(self, status):
        print('tweet:', status.text)
        tweet = status._json
        try:
            self.db[tweet['id_str']] = {"keyword": str(self.keyword), "location": str(self.location), "year": "2021",
                                        "text": str(tweet['text'])}
            self.count += 1
            if self.count >= self.max_count:
                return False
        except:
            print("skip: same id")
            pass

    def on_error(self, status_code):
        print("error code:", status_code)
        return True

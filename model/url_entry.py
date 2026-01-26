class UrlEntry:

    def __init__(self, short, long_url, clicks=0):
        self.short = short
        self.long_url = long_url
        self.clicks = clicks

    def increment(self):
        self.clicks += 1

    def to_dict(self):
        return {
            "short": self.short,
            "long_url": self.long_url,
            "clicks": self.clicks
        }

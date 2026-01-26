import random
import string
from model.url_entry import UrlEntry
from storage.json_storage import JsonStorage
from storage.analytics_exporter import AnalyticsExporter


class UrlRepository:

    def __init__(self):
        self.urls = {}
        self.storage = JsonStorage()
        self.exporter = AnalyticsExporter()

    def _generate_short_code(self, length=6):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def create_short_url(self, long_url):
        short = self._generate_short_code()
        self.urls[short] = UrlEntry(short, long_url)
        return short

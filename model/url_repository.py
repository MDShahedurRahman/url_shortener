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

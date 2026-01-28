from model.url_repository import UrlRepository
from view.url_view import UrlView


class UrlController:

    def __init__(self):
        self.repo = UrlRepository()
        self.view = UrlView()

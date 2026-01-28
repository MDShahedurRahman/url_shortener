from model.url_repository import UrlRepository
from view.url_view import UrlView


class UrlController:

    def __init__(self):
        self.repo = UrlRepository()
        self.view = UrlView()

    def run(self):
        while True:
            choice = self.view.show_menu()

            if choice == "1":
                self.create_short_url()
            elif choice == "2":
                self.resolve_url()
            elif choice == "3":
                self.show_all_urls()
            elif choice == "4":
                self.delete_url()
            elif choice == "5":
                self.export_analytics()
            elif choice == "6":
                self.save_data()
            elif choice == "7":
                self.load_data()
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid option")

    def create_short_url(self):
        long_url = self.view.get_long_url()
        short = self.repo.create_short_url(long_url)
        self.view.show_message(f"Short URL created: {short}")

    def resolve_url(self):
        short = self.view.get_short_url()
        long_url = self.repo.resolve(short)
        if long_url:
            self.view.show_message(f"Redirects to: {long_url}")
        else:
            self.view.show_message("Short URL not found")

    def show_all_urls(self):
        urls = self.repo.get_all()
        self.view.display_urls(urls)

    def delete_url(self):
        short = self.view.get_short_url()
        if self.repo.delete(short):
            self.view.show_message("URL deleted")
        else:
            self.view.show_message("Short URL not found")

    def export_analytics(self):
        self.repo.export_analytics()
        self.view.show_message("Analytics exported")

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

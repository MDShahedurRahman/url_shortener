class UrlView:

    def show_menu(self):
        print("\n--- URL Shortener ---")
        print("1. Create Short URL")
        print("2. Resolve Short URL")
        print("3. Show All URLs")
        print("4. Delete URL")
        print("5. Export Analytics")
        print("6. Save Data")
        print("7. Load Data")
        print("0. Exit")
        return input("Select option: ").strip()

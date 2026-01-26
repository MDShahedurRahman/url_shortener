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

    def get_long_url(self):
        return input("Enter long URL: ").strip()

    def get_short_url(self):
        return input("Enter short code: ").strip()

    def display_urls(self, urls):
        if not urls:
            print("No URLs found.")
            return

        for u in urls:
            print(f"{u.short} → {u.long_url} | clicks: {u.clicks}")

    def show_message(self, msg):
        print(msg)
